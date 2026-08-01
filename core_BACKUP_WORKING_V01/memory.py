class Memory:
    def __init__(self):
        self.history = []

    def remember(self, message, result):
        self.history.append({
            "message": message,
            "result": result
        })

    def recall(self):
        return self.history


memory = Memory()