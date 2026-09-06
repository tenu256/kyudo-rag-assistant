import ollama

from src.rag.vector_store import VectorStore


question = "会とは何ですか？"

response = ollama.embed(
    model="qwen3-embedding:0.6b",
    input=question,
)

query_embedding = response["embeddings"][0]

store = VectorStore()

results = store.collection.query(
    query_embeddings=[query_embedding],
    n_results=2,
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i, (document, metadata, distance) in enumerate(
    zip(documents, metadatas, distances),
    start=1,
):
    print(f"\n--- Result {i} ---")
    print(f"source: {metadata['source']}")
    print(f"chunk_index: {metadata['chunk_index']}")
    print(f"distance: {distance}")
    print(document)