import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

load_dotenv()

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from rag.agent import build_rag_graph
from rag.index import load_index


DATASET_PATH = REPO_ROOT / "tests" / "benchmark_dataset.json"
LIBRARIES = ["pypdf", "langchain", "pandas", "scikit-learn", "tensorflow"]


def _load_dataset(library: str | None = None) -> list[dict]:
    with open(DATASET_PATH) as f:
        cases = json.load(f)
    if library:
        cases = [c for c in cases if c["library"] == library]
    return cases


def _call_llm(question: str, docs: list) -> str:
    from rag.generate import _assemble_context
    context_text = _assemble_context(docs, "unknown")

    provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    if provider == "groq":
        llm = ChatGroq(model=os.getenv("GENERATION_MODEL", "llama-3.3-70b-versatile"))
    else:
        llm = ChatGoogleGenerativeAI(model=os.getenv("GENERATION_MODEL", "gemini-2.5-pro"))

    response = llm.invoke([
        ("system", "You are a code generation assistant. Answer using only the provided documentation."),
        ("human", f"Documentation:\n{context_text}\n\nQuestion: {question}"),
    ])
    return response.content


def naive_pipeline(question: str, library: str) -> str:
    """Semantic search with no version filter — baseline."""
    try:
        vector_db = load_index()
    except Exception:
        vector_db = load_index(library)
    docs = vector_db.similarity_search(question, k=3)
    return _call_llm(question, docs)


def versioned_pipeline(case: dict) -> str:
    """Full version-aware RAG pipeline."""
    graph = build_rag_graph()
    state = {
        "question": case["query"],
        "library": None,
        "version": None,
        "context": [],
        "answer": "",
    }
    result = graph.invoke(state)
    return result.get("answer", "")


def score_response(response: str, correct_api: str, wrong_api: str) -> int:
    has_correct = correct_api in response
    has_wrong = wrong_api in response
    return 1 if (has_correct and not has_wrong) else 0


def run_benchmark(cases: list[dict], pipeline: str) -> dict:
    results = {"naive": [], "versioned": []}

    for i, case in enumerate(cases):
        lib = case["library"]
        ver = case["version"]
        q = case["query"]
        correct = case["correct_api"]
        wrong = case["wrong_api"]

        print(f"  [{i+1}/{len(cases)}] {lib} {ver} | {q[:60]}...")

        if pipeline in ("naive", "both"):
            try:
                resp = naive_pipeline(q, lib)
                score = score_response(resp, correct, wrong)
            except Exception as e:
                print(f"    naive error: {e}")
                score = 0
            results["naive"].append({**case, "score": score})

        if pipeline in ("versioned", "both"):
            try:
                resp = versioned_pipeline(case)
                score = score_response(resp, correct, wrong)
            except Exception as e:
                print(f"    versioned error: {e}")
                score = 0
            results["versioned"].append({**case, "score": score})

    return results


def _accuracy(scored: list[dict]) -> float:
    if not scored:
        return 0.0
    return sum(c["score"] for c in scored) / len(scored)


def _format_table(results: dict, pipeline: str) -> str:
    lines = []
    lines.append(f"{'Library':<14} | {'Naive RAG':^9} | {'Version-Aware RAG':^17} | {'Delta':^7}")
    lines.append(f"{'-'*14}-|-{'-'*9}-|-{'-'*17}-|-{'-'*7}")

    all_libs = sorted({c["library"] for c in (results["naive"] or results["versioned"])})

    for lib in all_libs:
        naive_cases = [c for c in results["naive"] if c["library"] == lib]
        versioned_cases = [c for c in results["versioned"] if c["library"] == lib]

        naive_pct = f"{_accuracy(naive_cases)*100:.0f}%" if naive_cases else "--"
        ver_pct = f"{_accuracy(versioned_cases)*100:.0f}%" if versioned_cases else "--"

        if naive_cases and versioned_cases:
            delta = (_accuracy(versioned_cases) - _accuracy(naive_cases)) * 100
            delta_str = f"{delta:+.0f}pp"
        else:
            delta_str = "--"

        lines.append(f"{lib:<14} | {naive_pct:^9} | {ver_pct:^17} | {delta_str:^7}")

    naive_all = results["naive"]
    ver_all = results["versioned"]
    overall_naive = f"{_accuracy(naive_all)*100:.0f}%" if naive_all else "--"
    overall_ver = f"{_accuracy(ver_all)*100:.0f}%" if ver_all else "--"
    if naive_all and ver_all:
        overall_delta = f"{(_accuracy(ver_all) - _accuracy(naive_all))*100:+.0f}pp"
    else:
        overall_delta = "--"

    lines.append(f"{'-'*14}-|-{'-'*9}-|-{'-'*17}-|-{'-'*7}")
    lines.append(f"{'OVERALL':<14} | {overall_naive:^9} | {overall_ver:^17} | {overall_delta:^7}")

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run accuracy benchmark for version-aware RAG.")
    parser.add_argument("--library", choices=LIBRARIES, help="Benchmark one library only.")
    parser.add_argument(
        "--pipeline",
        choices=["naive", "versioned", "both"],
        default="both",
        help="Which pipeline(s) to evaluate.",
    )
    parser.add_argument("--output", help="Write markdown report to this file path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases = _load_dataset(args.library)

    if not cases:
        print(f"No benchmark cases found for library={args.library}.")
        return

    target = f"{args.library or 'all libraries'}"
    print(f"Running {args.pipeline} pipeline(s) on {len(cases)} cases for {target}...\n")

    results = run_benchmark(cases, args.pipeline)
    table = _format_table(results, args.pipeline)

    print("\n" + table)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(f"# Benchmark Report\n\n```\n{table}\n```\n")
        print(f"\nReport written to {out_path}")


if __name__ == "__main__":
    main()
