class SynthesisAgent:

    def __init__(self):
        self.name = "SCS Synthesis Agent"
        self.role = "integration"


    def synthesize(self, question, left_result, right_result):

        left_text = (
            left_result.get("response", "")
            if isinstance(left_result, dict)
            else str(left_result)
        )

        right_text = (
            right_result.get("response", "")
            if isinstance(right_result, dict)
            else str(right_result)
        )

        return {
            "agent": self.name,
            "role": self.role,
            "status": "complete",
            "response": (
                "Combined reasoning:\n\n"
                "LEFT:\n"
                + left_text
                + "\n\nRIGHT:\n"
                + right_text
            ),
            "confidence": 0.75
        }


synthesis_agent = SynthesisAgent()