class LearningAgent:
    def __init__(self):
        self.name = "Learning Agent"
        self.role = "feedback_and_optimization"

    def learn(self, history):
        if not history:
            return {
                "agent": self.name,
                "status": "no_history",
                "history_entries": 0,
                "lessons": []
            }

        lessons = []

        for entry in history:
            result = entry.get("result", {})
            results = result.get("results", {})

            for agent_name, agent_result in results.items():
                text = str(agent_result).lower()

                if "error" in text or "failed" in text:
                    lessons.append({
                        "type": "failure",
                        "agent": agent_name,
                        "problem": "The component encountered an error.",
                        "likely_cause": "Connection, configuration, or runtime problem.",
                        "recommendation": "Check dependencies and connection before retrying.",
                        "action": "Inspect and test the failing component.",
                        "confidence": "medium"
                    })

                if "verified': false" in text or '"verified": false' in text:
                    lessons.append({
                        "type": "verification",
                        "agent": agent_name,
                        "problem": "The output contained an unverified claim.",
                        "likely_cause": "Evidence or source information was insufficient.",
                        "recommendation": "Require supporting evidence before accepting the claim.",
                        "action": "Send the claim through verification.",
                        "confidence": "high"
                    })

        return {
            "agent": self.name,
            "role": self.role,
            "status": "analysed",
            "history_entries": len(history),
            "lessons": lessons
        }


learning_agent = LearningAgent()