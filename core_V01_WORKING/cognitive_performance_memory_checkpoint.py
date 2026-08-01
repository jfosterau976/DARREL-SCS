class CognitivePerformanceMemory:

    def __init__(self):
        self.name = "SCS Cognitive Performance Memory"
        self.records = []


    def evaluate(self, question, strategy, feedback):

        score = 0.8 if feedback else 0.5

        record = {
            "question": question,
            "strategy": strategy,
            "performance_score": score,
            "feedback": feedback
        }

        self.records.append(record)

        return {
            "system": self.name,
            "performance_score": score,
            "strategy": strategy,
            "status": "performance_recorded",
            "total_records": len(self.records)
        }


cognitive_performance_memory = CognitivePerformanceMemory()