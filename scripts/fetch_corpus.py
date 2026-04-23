import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import git


LIBRARY_REGISTRY = {
    "pypdf": {
        "repo": "https://github.com/py-pdf/pypdf.git",
        "doc_dirs": ["docs", "Documentation"],
        "tags": ["1.26.0", "2.12.1", "3.0.0", "3.17.4"],
    },
    "langchain": {
        "repo": "https://github.com/langchain-ai/langchain.git",
        "doc_dirs": ["docs"],
        # 0.1.0 uses v-prefix; 0.2+ use package==version format
        "tags": ["v0.1.0", "langchain==0.2.0", "langchain==0.3.0"],
    },
    "pandas": {
        "repo": "https://github.com/pandas-dev/pandas.git",
        "doc_dirs": ["doc/source"],
        "tags": ["v1.5.3", "v2.0.0", "v2.2.0"],
    },
    "scikit-learn": {
        "repo": "https://github.com/scikit-learn/scikit-learn.git",
        "doc_dirs": ["doc"],
        "tags": ["1.2.2", "1.3.0", "1.4.0"],
    },
    "tensorflow": {
        "repo": "https://github.com/tensorflow/tensorflow.git",
        "doc_dirs": ["docs"],
        # v2.16.1 is the correct tag; v2.16.0 was never tagged
        # WARNING: TF repo is ~3 GB of git objects — requires significant free disk space
        "tags": ["v2.12.0", "v2.15.0", "v2.16.1"],
        "filter": "blob:none",  # blobless clone to reduce disk usage
    },
}


def normalize_version(tag: str) -> str:
    # Handle "package==X.Y.Z" format (e.g. LangChain monorepo tags)
    if "==" in tag:
        return tag.split("==", 1)[1]
    return tag.lstrip("v")


def has_any_files(path: Path) -> bool:
    return path.exists() and any(child.is_file() for child in path.rglob("*"))


def convert_rst_fallback(content: str) -> str:
    # Minimal fallback when pandoc is unavailable.
    content = re.sub(r"(?m)^\s*\.\.\s+\w+::.*$", "", content)
    content = re.sub(r"(?m)^\s*:[\w-]+:.*$", "", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip() + "\n"


def convert_rst_to_markdown(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc",
        "-f",
        "rst",
        "-t",
        "markdown",
        str(src),
        "-o",
        str(dst),
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        dst.write_text(
            convert_rst_fallback(src.read_text(encoding="utf-8", errors="ignore")),
            encoding="utf-8",
        )


def discover_doc_dirs(repo_root: Path, configured_doc_dirs: list[str]) -> list[Path]:
    discovered: list[Path] = []

    for rel_path in configured_doc_dirs:
        candidate = repo_root / rel_path
        if candidate.exists() and candidate.is_dir():
            discovered.append(candidate)

    if discovered:
        return discovered

    # Fallback for older tags where docs path names differ (e.g., Doc/docs/source docs).
    for child in repo_root.iterdir():
        if child.is_dir() and "doc" in child.name.lower():
            discovered.append(child)

    return discovered


def fetch_library(
    library_name: str, config: dict, corpus_root: Path, force: bool = False
) -> None:
    print(f"\n[{library_name}] cloning {config['repo']}")
    clone_kwargs: dict = {"no_checkout": True}
    if config.get("filter"):
        clone_kwargs["multi_options"] = [f"--filter={config['filter']}"]
    with tempfile.TemporaryDirectory(prefix=f"{library_name}-repo-") as tmp_dir:
        repo = git.Repo.clone_from(config["repo"], tmp_dir, **clone_kwargs)
        repo_root = Path(tmp_dir)

        for tag in config["tags"]:
            normalized_version = normalize_version(tag)
            out_dir = corpus_root / library_name / normalized_version

            if has_any_files(out_dir) and not force:
                print(f"[{library_name} {tag}] skipped (already populated): {out_dir}")
                continue

            if force and out_dir.exists():
                shutil.rmtree(out_dir)
            out_dir.mkdir(parents=True, exist_ok=True)

            print(f"[{library_name} {tag}] checkout")
            try:
                repo.git.checkout(tag, force=True)
            except git.GitCommandError as exc:
                print(f"[{library_name} {tag}] checkout failed: {exc}")
                continue

            md_count = 0
            rst_count = 0
            collected_count = 0

            source_dirs = discover_doc_dirs(repo_root, config["doc_dirs"])
            if not source_dirs:
                print(
                    f"[{library_name} {tag}] no documentation directories found; scanning repository root"
                )
                source_dirs = [repo_root]

            for source_dir in source_dirs:

                for src in source_dir.rglob("*"):
                    if not src.is_file():
                        continue

                    suffix = src.suffix.lower()
                    if suffix not in {".md", ".rst"}:
                        continue

                    rel = src.relative_to(source_dir)
                    if suffix == ".md":
                        dst = out_dir / rel
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(src, dst)
                        md_count += 1
                    else:
                        dst = (out_dir / rel).with_suffix(".md")
                        convert_rst_to_markdown(src, dst)
                        rst_count += 1

                    collected_count += 1

            print(
                f"[{library_name} {tag}] collected={collected_count} "
                f"(md={md_count}, rst={rst_count}) -> {out_dir}"
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch versioned documentation corpus from library git tags."
    )
    parser.add_argument(
        "--library",
        choices=sorted(LIBRARY_REGISTRY.keys()),
        help="Fetch one library only.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-fetch even if output corpus already exists.",
    )
    parser.add_argument(
        "--corpus-root",
        default="./corpus",
        help="Corpus root directory (default: ./corpus).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    corpus_root = Path(args.corpus_root)
    corpus_root.mkdir(parents=True, exist_ok=True)

    selected = [args.library] if args.library else list(LIBRARY_REGISTRY.keys())
    for library_name in selected:
        fetch_library(
            library_name,
            LIBRARY_REGISTRY[library_name],
            corpus_root=corpus_root,
            force=args.force,
        )


if __name__ == "__main__":
    main()
