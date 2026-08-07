class DecisionEngine:

    def __init__(self):
        self.name = "SCS Executive Decision Engine"

    def decide(
        self,
        question,
        synthesis,
        verification
    ):

        verdict = verification.get(
            "verdict",
            "UNKNOWN"
        )

        confidence = verification.get(
            "confidence",
            0
        )

        if verdict == "PASS":

            action = "accept_answer"

        elif confidence >= 0.75:

            action = "accept_with_improvements"

        else:

            action = "request_another_pulse"

        return {

            "system": self.name,

            "question": question,

            "decision": action,

            "confidence": confidence,

            "verdict": verdict,

            "answer": synthesis,

            "status": "decision_complete"

        }


decision_engine = DecisionEngine()