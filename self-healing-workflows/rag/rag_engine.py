import json
import os

class RAGEngine:
    def __init__(self, path="rag/vector_store.json"):
        self.path = path

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    def store_failure(self, failure, solution):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append({
            "failure": failure,
            "solution": solution
        })

        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def retrieve_solution(self, failure):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
        except:
            return None

        for item in reversed(data):  # latest first
            if failure in item["failure"]:
                return item["solution"]

        return None