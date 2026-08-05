class DecisionRouter:
    def __init__(self):
        self.name = "Decision Router"

    def decide(self, message):
        text = message.lower()

        skills = []

        if any(word in text for word in [
            "idea", "creative", "imagine", "design"
        ]):
            skills.append("creativity")

        if any(word in text for word in [
            "check", "verify", "fact", "true", "claim"
        ]):
            skills.append("verification")

        if any(word in text for word in [
            "analyse", "analyze", "compare", "evaluate"
        ]):
            skills.append("analysis")

        if any(word in text for word in [
            "research", "latest", "news", "information"
        ]):
            skills.append("research")

        return {
            "router": self.name,
            "skills_needed": skills
        }


decision_router = DecisionRouter()