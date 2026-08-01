from core.cognitive_memory import cognitive_memory


class AdaptiveLearningLoop:

    def __init__(self):
        self.name = "SCS Adaptive Learning Loop"


    def learn(self, question, pulse_result):

        verification = pulse_result.get(
            "verification",
            {}
        )

        verdict = verification.get(
            "verdict",
            "UNKNOWN"
        )

        strategy = "LEFT+RIGHT+SYNTHESIS"

        memory_entry = {
            "question": question,
            "verdict": verdict,
            "strategy": strategy
        }

        stored = cognitive_memory.store(
            memory_entry
        )

        return {
            "system": self.name,
            "learning_status": "updated",
            "memory_result": stored
        }


adaptive_learning_loop = AdaptiveLearningLoop()