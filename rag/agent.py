import os
from typing import TypedDict

from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langgraph.graph import END, START, StateGraph
from packaging.version import InvalidVersion, Version
from pydantic import BaseModel, Field

from rag.generate import generation_node
from rag.index import load_index


class RAGState(TypedDict):
    question: str
    library: str | None
    version: str | None
    context: list[Document]
    answer: str


class IntentExtraction(BaseModel):
    library: str | None = Field(
        None,
        description="The Python library name, normalised to lowercase (e.g. 'pypdf', 'pandas')",
    )
    version: str | None = Field(
        None,
        description="The explicit version string the user mentioned (e.g. '3.17.4'), or null if not stated",
    )


INTENT_SYSTEM_PROMPT = """
You are a query parser. Extract the Python library name and version from the user's
question. Return null for version if the user does not explicitly state one.
Do NOT infer or guess a version. Only extract what the user explicitly wrote.

Library names must be normalised to lowercase:
  'PyPDF2' -> 'pypdf', 'Pandas' -> 'pandas', 'sklearn' -> 'scikit-learn',
  'TensorFlow' -> 'tensorflow', 'LangChain' -> 'langchain'
""".strip()


def resolve_latest_version(library: str, corpus_root: str = "./corpus") -> str:
    lib_path = os.path.join(corpus_root, library)
    versions = []
    for d in os.listdir(lib_path):
        try:
            versions.append(Version(d.lstrip("v")))
        except InvalidVersion:
            continue
    if not versions:
        raise ValueError(f"No indexed versions found for library: {library}")
    return str(max(versions))


def intent_extraction_node(state: RAGState) -> RAGState:
    provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    if provider == "groq":
        model_name = os.getenv("INTENT_MODEL", "llama-3.1-8b-instant")
        llm = ChatGroq(model=model_name)
    else:
        model_name = os.getenv("INTENT_MODEL", "gemini-2.5-flash")
        llm = ChatGoogleGenerativeAI(model=model_name)
    structured_llm = llm.with_structured_output(IntentExtraction)
    extraction: IntentExtraction = structured_llm.invoke(
        [
            ("system", INTENT_SYSTEM_PROMPT),
            ("human", state["question"]),
        ]
    )
    return {**state, "library": extraction.library, "version": extraction.version}


def version_aware_retriever_node(state: RAGState) -> RAGState:
    library = state.get("library")
    version = state.get("version")

    if not library:
        return {
            **state,
            "answer": "Could not determine the target library from your query.",
            "context": [],
        }

    if not version:
        try:
            version = resolve_latest_version(library)
        except Exception as exc:
            return {
                **state,
                "answer": f"Failed to resolve latest version for {library}: {exc}",
                "context": [],
            }

    filter_dict = {"library": library, "version": version}
    search_kwargs = {"filter": filter_dict, "k": 3, "fetch_k": 100}

    try:
        try:
            vector_db = load_index()
        except Exception:
            # Allows Phase-by-phase development when only a per-library index exists.
            vector_db = load_index(library)
        docs = vector_db.similarity_search(state["question"], **search_kwargs)
    except Exception as exc:
        return {**state, "answer": f"Retrieval failed: {exc}", "context": []}

    if not docs:
        return {
            **state,
            "answer": (
                f"No documentation found for {library} version {version}. "
                "Check that this version is indexed."
            ),
            "context": [],
        }

    return {**state, "context": docs, "version": version}


def build_rag_graph():
    graph = StateGraph(RAGState)
    graph.add_node("extract_intent", intent_extraction_node)
    graph.add_node("retrieve", version_aware_retriever_node)
    graph.add_node("generate", generation_node)

    graph.add_edge(START, "extract_intent")
    graph.add_edge("extract_intent", "retrieve")
    graph.add_conditional_edges(
        "retrieve",
        lambda s: "done" if s.get("answer") else "generate",
        {"generate": "generate", "done": END},
    )
    graph.add_edge("generate", END)

    return graph.compile()
