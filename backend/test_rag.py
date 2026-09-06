import ollama

from src.rag.vector_store import VectorStore


question = "会とは何ですか？"

# 質問をEmbedding
response = ollama.embed(
    model="qwen3-embedding:0.6b",
    input=question,
)

query_embedding = response["embeddings"][0]

# 関連チャンクを検索
store = VectorStore()

results = store.collection.query(
    query_embeddings=[query_embedding],
    n_results=2,
)

documents = results["documents"][0]

context = "\n\n---\n\n".join(documents)

# RAG用プロンプト
prompt = f"""
以下の参考資料だけを使って質問に答えてください。

参考資料:
{context}

質問:
{question}

回答ルール:
- 参考資料に書かれている内容を優先する
- 資料にない内容を勝手に追加しない
- 簡潔に日本語で回答する
"""

# ローカルLLMで回答生成
answer = ollama.chat(
    model="qwen3.5:4b",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    think=False,
)

print("\n=== Question ===")
print(question)

print("\n=== RAG Answer ===")
print(answer["message"]["content"])