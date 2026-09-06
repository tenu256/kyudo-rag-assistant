from fastapi import FastAPI
from pydantic import BaseModel
import ollama

from src.rag.vector_store import VectorStore


app = FastAPI(
    title="Kyudo RAG API",
    description="Backend API for Kyudo RAG Assistant",
    version="0.2.0",
)


class ChatRequest(BaseModel):
    message: str


class Source(BaseModel):
    source: str
    chunk_index: int


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]


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


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    # 1. 質問文をEmbedding
    embedding_response = ollama.embed(
        model="qwen3-embedding:0.6b",
        input=request.message,
    )

    query_embedding = embedding_response["embeddings"][0]

    # 2. ChromaDBから関連チャンクを検索
    store = VectorStore()

    results = store.collection.query(
        query_embeddings=[query_embedding],
        n_results=2,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # 3. 検索結果をLLM用コンテキストに変換
    context = "\n\n---\n\n".join(documents)

    prompt = f"""
以下の参考資料だけを使って質問に答えてください。

参考資料:
{context}

質問:
{request.message}

回答ルール:
- 参考資料に書かれている内容を優先する
- 資料にない内容を勝手に追加しない
- 分からない場合は「資料からは確認できません」と回答する
- 簡潔に日本語で回答する
"""

    # 4. ローカルLLMで回答生成
    response = ollama.chat(
        model="qwen3.5:4b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        think=False,
    )

    sources = [
        Source(
            source=metadata["source"],
            chunk_index=metadata["chunk_index"],
        )
        for metadata in metadatas
    ]

    return ChatResponse(
        answer=response["message"]["content"],
        sources=sources,
    )