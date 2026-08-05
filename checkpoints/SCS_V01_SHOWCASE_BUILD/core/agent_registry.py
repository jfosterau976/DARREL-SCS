class AgentRegistry:
    def __init__(self):
        self.name = "Agent Registry"

        self.registry = {
            "right_brain": {
                "role": "creative_thinking",
                "skills": [
                    "creativity",
                    "ideas",
                    "innovation"
                ],
                "status": "available"
            },

            "verifier_agent": {
                "role": "verification",
                "skills": [
                    "verification",
                    "fact_checking"
                ],
                "status": "available"
            },

            "left_brain": {
                "role": "analysis",
                "skills": [
                    "analysis",
                    "logic",
                    "reasoning"
                ],
                "status": "available"
            },

            "research_agent": {
                "role": "research",
                "skills": [
                    "research",
                    "information"
                ],
                "status": "available"
            }
        }

    def add_agent(self, name, role, skills):
        self.registry[name] = {
            "role": role,
            "skills": skills,
            "status": "available"
        }

    def get_agent(self, name):
        return self.registry.get(name)

    def find_by_skill(self, skill):
        matches = []

        for name, data in self.registry.items():
            if skill in data["skills"]:
                matches.append(name)

        return matches

    def list_all(self):
        return self.registry


agent_registry = AgentRegistry()