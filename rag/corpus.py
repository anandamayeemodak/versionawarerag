from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader


def load_versioned_corpus(library: str, root_dir: str) -> list[Document]:
    """
    Load all versioned docs for a library, injecting metadata on every chunk.
    root_dir should be the path to corpus/<library>/
    """
    library_root = Path(root_dir)
    if not library_root.exists() or not library_root.is_dir():
        raise FileNotFoundError(f"Corpus root not found for {library}: {root_dir}")

    all_chunks: list[Document] = []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        add_start_index=True,
    )

    for version_dir in sorted(p for p in library_root.iterdir() if p.is_dir()):
        for md_path in sorted(version_dir.rglob("*.md")):
            loader = UnstructuredMarkdownLoader(str(md_path))
            docs = loader.load()

            for doc in docs:
                # Inject metadata before splitting so child chunks inherit tags.
                doc.metadata["version"] = version_dir.name
                doc.metadata["library"] = library
                doc.metadata["source_file"] = md_path.name

            chunks = splitter.split_documents(docs)
            all_chunks.extend(chunks)

    for chunk in all_chunks:
        if not chunk.metadata.get("version"):
            raise ValueError(
                f"Chunk from {library} is missing version metadata: {chunk.metadata}"
            )
        if not chunk.metadata.get("library"):
            raise ValueError(
                f"Chunk from {library} is missing library metadata: {chunk.metadata}"
            )

    return all_chunks
