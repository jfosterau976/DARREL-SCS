from core.llm_interface import LLMInterface
from core.cognitive_message import create_message


class VerifierAgent:

    def __init__(self):
        self.name = "Verifier Agent"
        self.role = "verification"

        self.llm = LLMInterface(
            "Verifier Model",
            "local",
            "qwen3:4b"
        )

    def check(self, result):

        if hasattr(result, "to_dict"):
            data = result.to_dict()
            content = data.get("content", "")
        else:
            content = str(result)

        prompt = (
            "Check this AI claim for unsupported certainty "
            "or missing evidence.\n\n"
            "CLAIM:\n"
            + content
            + "\n\n"
            "Reply with either PASS or REVIEW, followed by "
            "one short reason."
        )

        response = self.llm.generate(prompt)

        text = response.get(
            "response",
            ""
        ).strip()

        if not text:

            error = response.get(
                "error",
                "No response returned."
            )

            return create_message(
                self.name,
                self.role,
                f"Verifier error: {error}",
                status="needs_verification",
                confidence=0.0,
                concerns=[error],
                metadata={
                    "verdict": "REVIEW",
                    "target": "LEFT",
                    "raw_response": ""
                }
            )

        upper = text.upper()

        if "REVIEW" in upper:
            verdict = "REVIEW"
        elif "PASS" in upper:
            verdict = "PASS"
        else:
            verdict = "REVIEW"

        # For V0.6, verification of a claim
        # returns feedback to LEFT by default.
        target = "LEFT"

        status = (
            "verified"
            if verdict == "PASS"
            else "needs_verification"
        )

        return create_message(
            self.name,
            self.role,
            text,
            status=status,
            confidence=0.90,
            concerns=[] if verdict == "PASS"
            else [text],
            metadata={
                "verdict": verdict,
                "target": target,
                "raw_response": text
            }
        )


verifier_agent = VerifierAgent()