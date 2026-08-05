class FeedbackInterpreter:

    def __init__(self):
        self.name = "SCS Feedback Interpreter"

    def interpret(self, verification):

        if not verification:
            return {
                "status": "no_feedback",
                "next_objective": None,
                "strategy": None
            }

        if hasattr(verification, "to_dict"):
            data = verification.to_dict()
        elif isinstance(verification, dict):
            data = verification
        else:
            return {
                "status": "unknown_feedback",
                "next_objective": None,
                "strategy": None
            }

        metadata = data.get("metadata", {})

        verdict = metadata.get(
            "verdict",
            ""
        ).upper()

        target = metadata.get(
            "target"
        )

        response = metadata.get(
            "response",
            ""
        )

        if verdict == "PASS":

            return {
                "status": "verified",
                "next_objective": None,
                "strategy": "complete"
            }

        if verdict == "REVIEW":

            text = response.lower()

            if any(word in text for word in [
                "evidence",
                "study",
                "studies",
                "implementation",
                "empirical",
                "quantitative"
            ]):

                return {
                    "status": "needs_evidence",
                    "next_objective": (
                        "Find empirical evidence and "
                        "real-world implementations."
                    ),
                    "strategy": {
                        "left": True,
                        "right": False,
                        "synthesis": True,
                        "verifier": True
                    },
                    "target": target
                }

            return {
                "status": "needs_revision",
                "next_objective": (
                    "Improve the previous response "
                    "before verification."
                ),
                "strategy": {
                    "left": True,
                    "right": False,
                    "synthesis": True,
                    "verifier": True
                },
                "target": target
            }

        return {
            "status": "unknown_verdict",
            "next_objective": (
                "Reassess the previous response."
            ),
            "strategy": {
                "left": True,
                "right": True,
                "synthesis": True,
                "verifier": True
            },
            "target": target
        }


feedback_interpreter = FeedbackInterpreter()