import ollama

from src.rag.chunker import load_text, split_text
from src.rag.vector_store import VectorStore


text = load_text("data/sample/shaho_hassetsu.txt")
chunks = split_text(text)

response = ollama.embed(
    model="qwen3-embedding:0.6b",
    input=chunks,
)

embeddings = response["embeddings"]

store = VectorStore()

store.add_chunks(
    chunks=chunks,
    embeddings=embeddings,
    source="shaho_hassetsu.txt",
)

print(f"{len(chunks)} chunks saved to ChromaDB.")