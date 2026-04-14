def __init__(self, path="rag/vector_store.json"):
    self.path = path

    if not os.path.exists(self.path):
        with open(self.path, "w") as f:
            json.dump([], f)