class CognitiveStateManager:

    def __init__(self):
        self.name = "SCS Cognitive State Manager"


    def evaluate(self, question, confidence=0.5):

        q = question.lower()

        complexity = "medium"
        risk = "medium"

        if any(word in q for word in [
            "should",
            "risk",
            "invest",
            "decision",
            "important"
        ]):
            complexity = "high"
            risk = "high"

        if confidence >= 0.8:
            state = "confident"

        elif confidence <= 0.4:
            state = "uncertain"

        else:
            state = "balanced"


        return {
            "system": self.name,
            "question": question,
            "complexity": complexity,
            "risk": risk,
            "confidence": confidence,
            "cognitive_state": state
        }


cognitive_state = CognitiveStateManager()