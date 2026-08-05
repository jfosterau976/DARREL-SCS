class Router:
    def __init__(self):
        self.name = "Decision Router"

    def route(self, message):
        text = message.lower()
        targets = []

        research_words = [
            "research", "investigate", "find", "latest",
            "information", "current", "news", "web", "online"
        ]

        planning_words = [
            "plan", "planning", "steps", "strategy", "roadmap"
        ]

        creative_words = [
            "idea", "ideas", "creative", "imagine", "alternatives"
        ]

        analysis_words = [
            "compare", "analyse", "analyze",
            "evaluate", "assess"
        ]

        verification_words = [
            "verify", "verification", "fact check",
            "fact-check", "check facts", "source",
            "sources", "citation", "citations"
        ]

        if any(word in text for word in research_words):
            targets.extend(["left_brain", "research_agent", "verifier_agent"])

        if any(word in text for word in planning_words):
            targets.extend(["left_brain", "planning_agent"])

        if any(word in text for word in creative_words):
            targets.append("right_brain")

        if any(word in text for word in analysis_words):
            targets.append("left_brain")

        if any(word in text for word in verification_words):
            targets.append("verifier_agent")

        if not targets:
            targets = ["left_brain"]

        return list(dict.fromkeys(targets))


router = Router()