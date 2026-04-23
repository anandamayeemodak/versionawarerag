# Version-Aware Agentic RAG

**Course project — Anandamayee Modak, MS Engineering Management**

A retrieval-augmented generation (RAG) system that eliminates cross-version API hallucination in LLM-generated code. The system applies a hard metadata filter at retrieval time so that documentation chunks from version X can never influence answers for version Y.

---

## Problem

LLMs conflate API knowledge across library versions because their training corpora mix documentation indiscriminately. A model may confidently emit `PdfFileReader()` — a PyPDF2 v1.x method — in a pypdf v3.x environment, producing silently broken code with no syntax error. This is **temporal hallucination**.

## Hypothesis

Strict version-filtering at retrieval reduces API drift errors versus a standard non-versioned RAG pipeline. Results across five libraries show consistent **+10 percentage-point improvements** on libraries with breaking API changes (pypdf, LangChain, scikit-learn), with no regression on stable APIs (pandas, TensorFlow). Overall accuracy: 46% naive → 52% version-aware across 50 benchmark cases.

---

## Code Structure

```
├── main.py                        # Interactive CLI entry point
├── requirements.txt
├── .env.example                   # Environment variable template
│
├── rag/
│   ├── agent.py                   # LangGraph graph: intent extraction, migration, retrieval
│   ├── generate.py                # LLM generation node
│   ├── index.py                   # FAISS index build and load
│   └── corpus.py                  # Versioned doc loader with metadata injection
│
├── scripts/
│   ├── fetch_corpus.py            # Pulls versioned docs from library Git tags
│   ├── build_index.py             # Builds per-library and combined FAISS indexes
│   ├── benchmark.py               # Accuracy benchmark: naive vs version-aware pipeline
│   └── latency.py                 # Per-node latency profiler with acceptance thresholds
│
├── tests/
│   ├── benchmark_dataset.json     # 50 hand-verified test cases across 5 libraries
│   └── test_benchmark.py          # Pytest placeholder
│
└── corpus/                        # Created at runtime by fetch_corpus.py
    ├── pypdf/1.26.0/ ... 3.17.4/
    ├── langchain/0.1.0/ ... 0.3.0/
    ├── pandas/1.5.3/ ... 2.2.0/
    └── scikit-learn/1.2.2/ ... 1.4.0/
```

---

## Dependencies

Install all dependencies with:

```bash
pip install -r requirements.txt
```

Key packages:

| Package | Purpose |
|---|---|
| `langchain`, `langchain-community` | Document loaders, FAISS wrapper, text splitter |
| `langchain-huggingface` | Local embedding model via sentence-transformers |
| `langchain-groq` | Groq LLM provider (intent + generation) |
| `langchain-google-genai` | Gemini LLM provider (alternative) |
| `langgraph` | LangGraph stateful agent graph |
| `faiss-cpu` | Vector similarity search |
| `sentence-transformers` | `all-MiniLM-L6-v2` embedding model |
| `gitpython` | Clone library repos at specific tags |
| `unstructured[md]` | Markdown document loader |
| `packaging` | Semantic version comparison |
| `python-dotenv` | `.env` file loading |

---

## Environment Setup

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_gemini_api_key_here      # only needed if LLM_PROVIDER=gemini
HF_TOKEN=your_huggingface_token_here         # optional, for gated HF models
LLM_PROVIDER=groq                            # groq | gemini
INTENT_MODEL=llama-3.3-70b-versatile
GENERATION_MODEL=llama-3.3-70b-versatile
EMBED_MODEL=all-MiniLM-L6-v2
CORPUS_ROOT=./corpus
INDEX_ROOT=./indexes
```

**Groq rate limits for `llama-3.3-70b-versatile`:** 30 RPM, 12,000 TPM, 1,000 RPD. The benchmark script respects these with a configurable `--delay` flag (default 3 s between cases).

---

## Running the Project

### Step 1 — Fetch versioned documentation corpus

Downloads Markdown docs from library Git tags into `corpus/`. Already-populated versions are skipped automatically (idempotent).

```bash
# Fetch all libraries
py scripts/fetch_corpus.py

# Fetch one library only
py scripts/fetch_corpus.py --library pypdf

# Force re-fetch
py scripts/fetch_corpus.py --library pypdf --force
```

> **TensorFlow note:** The TensorFlow repo is ~3 GB of git objects. If your system temp drive lacks space, redirect the temp dir before running:
> ```powershell
> $env:TEMP = "D:\tmp"; $env:TMP = "D:\tmp"
> mkdir D:\tmp -Force
> py scripts/fetch_corpus.py --library tensorflow
> ```
> The script uses a blobless clone (`--filter=blob:none`) for TensorFlow to minimise download size.

No external dataset download is required beyond what this script performs. All documentation is fetched from public GitHub repositories at specific release tags listed in `LIBRARY_REGISTRY` inside `fetch_corpus.py`.

### Step 2 — Build FAISS indexes

The embedding model (`all-MiniLM-L6-v2`) is downloaded automatically from HuggingFace on first run (~90 MB, cached locally by `sentence-transformers`).

```bash
# Build indexes for all libraries individually
py scripts/build_index.py

# Build one library
py scripts/build_index.py --lib pypdf

# Build combined index (all libraries merged)
py scripts/build_index.py --combined
```

### Step 3 — Run the interactive CLI

```bash
py main.py
```

Example queries:
```
How do I open a PDF with pypdf 3.17.4?
How do I use PdfFileReader to read a PDF?     ← triggers migration node
How do I merge PDFs with pypdf?               ← auto-resolves to latest version
```

Type `exit` to quit.

### Step 4 — Run the accuracy benchmark

```bash
# Versioned pipeline only (~3 min, safe under Groq TPM limits)
py scripts/benchmark.py --library pypdf --pipeline versioned

# Both pipelines with markdown report (~8 min with safety delay)
py scripts/benchmark.py --library pypdf --pipeline both --delay 5 --output report.md
```

Acceptance threshold: ≥ 75% accuracy on the version-aware pipeline for pypdf.

### Step 5 — Run the latency profiler

```bash
py -X utf8 scripts/latency.py
```

Acceptance thresholds:
- Total end-to-end latency < 10,000 ms
- FAISS filtered search < 500 ms

---

## System Architecture

```
User query
    │
    ▼
[extract_intent]  ← LLM call: parses library name and version from natural language
    │
    ├─── deprecated API detected? ──► [migration]  ← augments question with migration note
    │                                      │
    ▼                                      ▼
[retrieve]  ← FAISS similarity_search with hard metadata filter {library, version}
    │                fetch_k=100 candidates → keep k=3 matching exact version
    │
    ├─── 0 results or error? ──► returns error message directly
    │
    ▼
[generate]  ← LLM call: produces version-correct code from filtered doc excerpts
    │
    ▼
Answer
```

The hard filter is applied **before** any context reaches the LLM. There is no soft fallback that drops the version constraint — if zero chunks match, the pipeline returns an explicit error rather than silently returning cross-version results.

---

## Attribution

### Code origin

All code in this repository was written from scratch for this project, guided by the implementation plan in `docs/version_aware_rag_plan.docx`. No code was copied verbatim from external repositories.

**Implementation plan as specification:** The plan document provided exact function signatures, algorithm logic, and architectural decisions. The code implements that specification. Sections that follow the plan closely are listed below.


### External libraries used (not copied, imported via pip)

- [LangChain](https://github.com/langchain-ai/langchain) — Apache 2.0
- [LangGraph](https://github.com/langchain-ai/langgraph) — MIT
- [FAISS](https://github.com/facebookresearch/faiss) — MIT
- [sentence-transformers](https://github.com/UKPLab/sentence-transformers) — Apache 2.0
- [Groq Python SDK](https://github.com/groq/groq-python) — Apache 2.0
- [GitPython](https://github.com/gitpython-developers/GitPython) — BSD

### Documentation corpus sources

All documentation is fetched at runtime from public GitHub repositories at specific release tags. No data is bundled in this repository.

| Library | Source | Tags fetched |
|---|---|---|
| pypdf | github.com/py-pdf/pypdf | 1.26.0, 2.12.1, 3.0.0, 3.17.4 |
| LangChain | github.com/langchain-ai/langchain | v0.1.0, langchain==0.2.0, langchain==0.3.0 |
| pandas | github.com/pandas-dev/pandas | v1.5.3, v2.0.0, v2.2.0 |
| scikit-learn | github.com/scikit-learn/scikit-learn | 1.2.2, 1.3.0, 1.4.0 |
| TensorFlow | github.com/tensorflow/tensorflow | v2.12.0, v2.15.0, v2.16.1 |

### Embedding model

`all-MiniLM-L6-v2` is downloaded automatically from HuggingFace (`sentence-transformers` library) on first index build. It is cached locally by the library and does not need to be downloaded manually. Size: ~90 MB.
