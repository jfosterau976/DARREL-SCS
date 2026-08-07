class AttentionManager:

    def __init__(self):
        self.name = "SCS Attention Manager"
        self.role = "priority_selection"

    def analyse_priority(self, message):

        message = message.lower()
        priorities = []

        if any(word in message for word in [
            "safe",
            "safety",
            "risk",
            "healthcare",
            "medical",
            "elderly",
            "security"
        ]):
            priorities.append({
                "area": "safety",
                "priority": "high",
                "reason": "Potential high-impact consequences detected."
            })

        if any(word in message for word in [
            "facts",
            "verify",
            "research",
            "evidence",
            "medical",
            "healthcare",
            "accuracy"
        ]):
            priorities.append({
                "area": "accuracy",
                "priority": "high",
                "reason": "Information quality requires checking."
            })

        if any(word in message for word in [
            "create",
            "invent",
            "idea",
            "design",
            "innovate",
            "future"
        ]):
            priorities.append({
                "area": "creativity",
                "priority": "medium",
                "reason": "Creative exploration is required."
            })

        if any(word in message for word in [
            "should",
            "compare",
            "versus",
            "instead",
            "advantages",
            "disadvantages",
            "strategy",
            "analyse",
            "analyze",
            "evaluate",
            "improve",
            "multiple",
            "specialised",
            "specialized"
        ]):
            priorities.append({
                "area": "analysis",
                "priority": "medium",
                "reason": "Comparative or strategic reasoning is required."
            })

        if not priorities:
            priorities.append({
                "area": "general_reasoning",
                "priority": "low",
                "reason": "Basic cognitive processing is sufficient."
            })

        return {
            "manager": self.name,
            "status": "attention_complete",
            "priorities": priorities
        }


attention_manager = AttentionManager()