# RAG-Demo-Application
Sample project created to understand Gen AI and RAG concepts. 

# Azure RAG Agent with Context Compression

Token-aware AI backend built with FastAPI and Azure, inspired by Headroom’s “context compression layer for AI agents”.  
This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) pipeline on Azure with a middleware that reduces prompt tokens while preserving answer quality.

---

## ✨ What this project does

- Provides a **FastAPI backend** with:
  - A `/upload` API to ingest documents, store them in Azure Blob Storage, and index them in Azure AI Search.
  - A `/chat` API that runs a **RAG workflow** (retrieve chunks from Azure AI Search, call Azure OpenAI for grounded answers).
- Implements a **context compression middleware** that:
  - Trims redundant RAG chunks.
  - Summarizes or prunes older conversation history.
  - Optionally integrates the Headroom `compress(messages)` library for advanced compression.
- Exposes a simple frontend (React / React Native) where you can:
  - Upload documents.
  - Ask questions.
  - See **token usage before vs after compression** for each request.

This is a small, interview-ready project to showcase:

- FastAPI + Python backend skills.
- Azure RAG architecture understanding.
- AI agent workflow design and token/context optimization.
- Integration of third-party tooling (Headroom-style compression) into a production-like stack.

---

## 🧠 Inspiration: Headroom

[Headroom](https://github.com/headroomlabs-ai/headroom) is an open-source context compression layer for AI agents. It can run as:

- A **library** – `compress(messages)` in Python/TypeScript.
- A **proxy** – route LLM traffic through a local process.
- A **agent wrapper** – integrate with popular AI tools and editors.
- An **MCP server** – exposing tools like `headroom_compress`, `headroom_retrieve`, etc.

Instead of reimplementing all of Headroom, this project borrows the **core idea**:

> “Compress as much as possible before the LLM sees any of it.”

Here, that means:
- Compressing RAG context (chunks retrieved from Azure AI Search).
- Compressing multi-turn chat history.
- Measuring and surfacing **token savings**.