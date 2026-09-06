from pathlib import Path


def load_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def split_text(text: str, chunk_size: int = 200, overlap: int = 40) -> list[str]:
    chunks: list[str] = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == text_length:
            break

        start = end - overlap

    return chunks