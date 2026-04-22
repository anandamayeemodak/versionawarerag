import os

from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    print("Version-Aware Agentic RAG")
    print("Project scaffold is ready. Implement phases 2-10 next.")
    print(f"CORPUS_ROOT={os.getenv('CORPUS_ROOT', './corpus')}")
    print(f"INDEX_ROOT={os.getenv('INDEX_ROOT', './indexes')}")


if __name__ == "__main__":
    main()
