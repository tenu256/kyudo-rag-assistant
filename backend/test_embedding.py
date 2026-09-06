import ollama

response = ollama.embed(
    model="qwen3-embedding:0.6b",
    input="弓道の射法八節とは何ですか？",
)

embedding = response["embeddings"][0]

print("ベクトル次元:", len(embedding))
print("先頭10要素:", embedding[:10])