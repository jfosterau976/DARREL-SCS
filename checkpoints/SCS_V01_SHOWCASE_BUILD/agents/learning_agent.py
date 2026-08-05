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


            if isinstance(result, list):
                results = {
                    str(i): item
                    for i, item in enumerate(result)
                }

            else:
                results = result.get("results", {})


            for agent_name, agent_result in results.items():

                text = str(agent_result).lower()


                if "error" in text or "failed" in text:
                    lessons.append({
                        "type": "failure",
                        "agent": agent_name,
                        "problem": "The component encountered an error.",
                        "recommendation": "Check dependencies and improve error handling.",
                        "confidence": "medium"
                    })


                if "verified': false" in text or '"verified": false' in text:
                    lessons.append({
                        "type": "verification",
                        "agent": agent_name,
                        "problem": "Unverified claim detected.",
                        "recommendation": "Require stronger evidence before acceptance.",
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