class OptimizerAgent:
    def __init__(self):
        self.name = "Optimizer Agent"
        self.role = "improvement_planning"

    def optimize(self, lessons):
        if not lessons:
            return {
                "agent": self.name,
                "status": "no_lessons",
                "recommendations": []
            }

        recommendations = []

        for lesson in lessons:
            if lesson.get("type") == "failure":
                recommendations.append({
                    "issue": lesson.get("problem"),
                    "proposal": "Add health checks and improve error handling for the failing component.",
                    "expected_benefit": "Reduce repeated failures and improve reliability.",
                    "risk": "low",
                    "test_required": "Run controlled tests before accepting changes."
                })

            if lesson.get("type") == "verification":
                recommendations.append({
                    "issue": lesson.get("problem"),
                    "proposal": "Require stronger evidence checks before accepting claims.",
                    "expected_benefit": "Improve accuracy and trustworthiness.",
                    "risk": "low",
                    "test_required": "Compare verified and unverified outputs."
                })

        return {
            "agent": self.name,
            "role": self.role,
            "status": "optimised",
            "recommendations": recommendations
        }


optimizer_agent = OptimizerAgent()