from fastapi import FastAPI

app = FastAPI(
    title="Azure RAG Agent with Context Compression",
    description="Token-aware RAG demo backend built with FastAPI and Azure.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat")
def chat_stub():
    # Placeholder: will later call Azure OpenAI + RAG
    return {"message": "Chat endpoint stub. RAG + compression to be implemented."}