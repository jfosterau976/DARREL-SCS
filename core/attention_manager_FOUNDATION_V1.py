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
            "design"
        ]):
            priorities.append({
                "area": "creativity",
                "priority": "medium",
                "reason": "New ideas or solutions required."
            })


        if not priorities:
            priorities.append({
                "area": "general_reasoning",
                "priority": "medium",
                "reason": "General cognitive processing."
            })


        return {
            "manager": self.name,
            "status": "attention_complete",
            "priorities": priorities
        }


attention_manager = AttentionManager()