class EvaluationAgent:
    def __init__(self):
        self.name = "Evaluation Agent"
        self.role = "testing_and_quality_control"

    def evaluate(self, proposal):
        if not proposal:
            return {
                "agent": self.name,
                "status": "no_proposal",
                "score": 0
            }

        score = 0
        checks = []

        text = str(proposal).lower()

        if "test" in text:
            score += 1
            checks.append("Includes testing plan")

        if "risk" in text:
            score += 1
            checks.append("Risk considered")

        if "benefit" in text or "improve" in text:
            score += 1
            checks.append("Expected benefit identified")

        if score >= 3:
            decision = "approved_for_testing"
        elif score >= 1:
            decision = "needs_review"
        else:
            decision = "rejected"

        return {
            "agent": self.name,
            "role": self.role,
            "status": decision,
            "score": score,
            "checks": checks,
            "note": "Proposal requires controlled testing before acceptance."
        }


evaluation_agent = EvaluationAgent()