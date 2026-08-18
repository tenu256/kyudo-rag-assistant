from fastapi import FastAPI

app = FastAPI(
    title="Kyudo RAG API",
    description="Backend API for Kyudo RAG Assistant",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "Kyudo RAG API is running"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }