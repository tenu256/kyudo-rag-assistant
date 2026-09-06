from src.rag.chunker import load_text, split_text

text = load_text("data/sample/shaho_hassetsu.txt")
chunks = split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)