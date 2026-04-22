import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from rag.corpus import load_versioned_corpus


_embeddings_cache: HuggingFaceEmbeddings | None = None


def get_embeddings() -> HuggingFaceEmbeddings:
    global _embeddings_cache
    if _embeddings_cache is None:
        model_name = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
        hf_token = os.getenv("HF_TOKEN")
        model_kwargs = {"token": hf_token} if hf_token else {}
        _embeddings_cache = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)
    return _embeddings_cache


def build_library_index(library: str, corpus_root: str, index_root: str) -> FAISS:
    """Build and persist a FAISS index for a single library."""
    chunks = load_versioned_corpus(library, os.path.join(corpus_root, library))
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    save_path = os.path.join(index_root, library)
    os.makedirs(save_path, exist_ok=True)
    vectorstore.save_local(save_path)
    print(f"Built index for {library}: {len(chunks)} chunks")
    return vectorstore


def build_combined_index(
    libraries: list[str], corpus_root: str, index_root: str
) -> FAISS:
    """Build and persist a single FAISS index merging all libraries."""
    all_chunks = []
    for library in libraries:
        all_chunks.extend(
            load_versioned_corpus(library, os.path.join(corpus_root, library))
        )

    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(all_chunks, embeddings)

    save_path = os.path.join(index_root, "combined")
    os.makedirs(save_path, exist_ok=True)
    vectorstore.save_local(save_path)
    print(f"Built combined index: {len(all_chunks)} total chunks")
    return vectorstore


def load_index(library: str | None = None, index_root: str = "./indexes") -> FAISS:
    """Load a persisted FAISS index from disk."""
    embeddings = get_embeddings()
    path = os.path.join(index_root, library if library else "combined")
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
