import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq


GENERATION_SYSTEM_PROMPT = """
You are a code generation assistant with access to official library documentation.

Rules:
1. Only use APIs that appear in the provided documentation excerpts.
2. Do not use any API that is not in the provided context, even if you know it exists
   in other versions.
3. Begin your response with a comment stating the library name and version.
4. If the documentation does not contain enough information to answer, say so
   explicitly rather than guessing.
5. Include import statements in all code examples.
""".strip()


def _assemble_context(docs: list, version: str) -> str:
    parts = []
    for i, doc in enumerate(docs):
        meta = doc.metadata
        header = (
            f"--- Excerpt {i + 1} | "
            f"library: {meta.get('library')} | "
            f"version: {meta.get('version')} | "
            f"file: {meta.get('source_file')} ---"
        )
        parts.append(f"{header}\n{doc.page_content}")
    return "\n\n".join(parts)


def generation_node(state: dict) -> dict:
    if state.get("answer"):
        return state

    if not state.get("context"):
        return {**state, "answer": "No context available to generate an answer."}

    version = state.get("version") or "unknown"
    library = state.get("library") or "unknown"
    context_text = _assemble_context(state["context"], version)

    provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    if provider == "groq":
        model_name = os.getenv("GENERATION_MODEL", "llama-3.3-70b-versatile")
        llm = ChatGroq(model=model_name)
    else:
        model_name = os.getenv("GENERATION_MODEL", "gemini-2.5-pro")
        llm = ChatGoogleGenerativeAI(model=model_name)
    response = llm.invoke(
        [
            ("system", GENERATION_SYSTEM_PROMPT),
            (
                "human",
                (
                    f"Target library: {library}\n"
                    f"Target version: {version}\n\n"
                    f"Documentation:\n{context_text}\n\n"
                    f"Question: {state['question']}"
                ),
            ),
        ]
    )
    return {**state, "answer": response.content}
