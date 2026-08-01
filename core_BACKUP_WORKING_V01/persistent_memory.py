import json
from pathlib import Path


class PersistentMemory:
    def __init__(self, filename="memory.json"):
        self.filename = Path(filename)
        self.history = self._load()

    def _load(self):
        if self.filename.exists():
            try:
                return json.loads(self.filename.read_text())
            except (json.JSONDecodeError, OSError):
                return []

        return []

    def remember(self, message, result):
        self.history.append({
            "message": message,
            "result": result
        })
        self._save()

    def _save(self):
        self.filename.write_text(
            json.dumps(self.history, indent=2)
        )

    def recall(self):
        return self.history


persistent_memory = PersistentMemory()