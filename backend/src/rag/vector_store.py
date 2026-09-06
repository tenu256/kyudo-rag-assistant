import chromadb


class VectorStore:
    def __init__(self, path: str = "chroma_db") -> None:
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(
            name="kyudo_documents"
        )

    def add_chunks(
        self,
        chunks: list[str],
        embeddings: list[list[float]],
        source: str,
    ) -> None:
        ids = [f"{source}-{i}" for i in range(len(chunks))]

        metadatas = [
            {
                "source": source,
                "chunk_index": i,
            }
            for i in range(len(chunks))
        ]

        self.collection.upsert(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )