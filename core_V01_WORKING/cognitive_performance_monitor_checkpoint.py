class CognitivePerformanceMonitor:

    def __init__(self):
        self.name = "SCS Cognitive Performance Monitor"
        self.history = []


    def evaluate(self, question, result):

        confidence = result.get(
            "confidence",
            0.5
        )

        status = "stable"

        if confidence < 0.4:
            status = "needs_more_reasoning"

        elif confidence > 0.8:
            status = "high_confidence"


        performance = {
            "question": question,
            "confidence": confidence,
            "performance_state": status,
            "modules_used": result.get(
                "activated_modules",
                []
            )
        }

        self.history.append(performance)

        return {
            "system": self.name,
            "evaluation": performance,
            "total_evaluations": len(self.history)
        }


performance_monitor = CognitivePerformanceMonitor()