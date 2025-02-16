import faiss


class FaissDB:
    def __init__(self, embedding_dim=128):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(self.embedding_dim)
        self.index = faiss.IndexIDMap(self.index)

    def store(self, ids, embeddings):
        self.index.add_with_ids(embeddings, ids)
        self.save()

    def load(self, path="faiss_index.ivf"):
        self.index = faiss.read_index(path)

    def save(self):
        faiss.write_index(self.index, "faiss_index.ivf")

    def search(self, query, k=1):
        ex, retrieved_ids = self.index.search(query, k=k)

        return ex, retrieved_ids
