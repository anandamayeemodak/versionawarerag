from dotenv import load_dotenv

load_dotenv(override=True)

from rag.agent import build_rag_graph


def main() -> None:
    print("Version-Aware Agentic RAG")
    print('Enter a code generation query. Type "exit" to quit.\n')

    chain = build_rag_graph()

    while True:
        try:
            question = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if question.lower() == "exit":
            break
        if not question:
            continue

        state = {
            "question": question,
            "library": None,
            "version": None,
            "context": [],
            "answer": "",
        }

        result = chain.invoke(state)
        print(f"\n{result['answer']}\n")


if __name__ == "__main__":
    main()
