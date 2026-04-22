import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Allow direct execution via `python scripts/build_index.py` from repo root.
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from rag.index import build_combined_index, build_library_index


LIBRARIES = ["pypdf", "langchain", "pandas", "scikit-learn", "tensorflow"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build FAISS indexes from versioned corpus."
    )
    parser.add_argument(
        "--lib", choices=LIBRARIES, help="Build one library index only."
    )
    parser.add_argument(
        "--combined",
        action="store_true",
        help="Build combined index for all libraries.",
    )
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()

    corpus_root = os.getenv("CORPUS_ROOT", "./corpus")
    index_root = os.getenv("INDEX_ROOT", "./indexes")

    if args.lib:
        build_library_index(args.lib, corpus_root, index_root)
        return

    if args.combined:
        build_combined_index(LIBRARIES, corpus_root, index_root)
        return

    for library in LIBRARIES:
        build_library_index(library, corpus_root, index_root)


if __name__ == "__main__":
    main()
