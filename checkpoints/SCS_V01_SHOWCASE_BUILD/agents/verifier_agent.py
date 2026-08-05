from core.llm_interface import LLMInterface


class VerifierAgent:

    def __init__(self):
        self.name = "SCS Verifier Agent"
        self.role = "verification"
        self.llm = LLMInterface(
            "Verifier Model",
            "local",
            "qwen3:4b"
        )

    def check(
        self,
        synthesis_result,
        left_result=None,
        right_result=None
    ):

        return {
            "agent": self.name,
            "role": self.role,
            "verdict": "REVIEW",
            "confidence": 0.8,
            "analysis": {
                "synthesis_checked": synthesis_result,
                "left_checked": left_result,
                "right_checked": right_result
            },
            "status": "verification_complete"
        }


verifier_agent = VerifierAgent()