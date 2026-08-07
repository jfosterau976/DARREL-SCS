from core.cognitive_memory import cognitive_memory


class LearningFeedback:

    def __init__(self):
        self.name = "SCS Learning Feedback"
        self.history = []

    def evaluate(self, performance):

        lessons = []

        verification = performance.get(
            "verification",
            {}
        )

        verdict = verification.get(
            "verdict",
            "UNKNOWN"
        )

        confidence = verification.get(
            "confidence",
            0
        )

        improvements = verification.get(
            "improvements",
            []
        )

        learned_reasoning = verification.get(
            "learned_reasoning_reviewed",
            []
        )

        if performance.get("synthesis"):
            lessons.append(
                "Synthesis successfully combined agent outputs"
            )

        if verification:
            lessons.append(
                "Verification layer completed self-review"
            )

        if verdict == "PASS":
            lessons.append(
                "Reasoning process passed verification"
            )

        elif verdict == "REVIEW":
            lessons.append(
                "Reasoning requires further improvement"
            )

        if learned_reasoning:
            lessons.append(
                "Learned reasoning contributed to decision making"
            )

        experience = {

            "type": "reasoning_feedback",

            "verdict": verdict,

            "confidence": confidence,

            "lessons": lessons,

            "improvements": improvements,

            "learned_reasoning": learned_reasoning,

            "strength": 1,

            "importance": (
                "HIGH"
                if confidence >= 0.90
                else "MEDIUM"
                if confidence >= 0.75
                else "LOW"
            )
        }

        memory_result = cognitive_memory.remember(
            experience
        )

        self.history.append(
            experience
        )

        return {

            "system": self.name,

            "status": "feedback_complete",

            "verdict": verdict,

            "confidence": confidence,

            "lessons": lessons,

            "improvements": improvements,

            "memory": memory_result,

            "experiences_stored": len(self.history)

        }

    def recall_lessons(self):

        return self.history


learning_feedback = LearningFeedback()