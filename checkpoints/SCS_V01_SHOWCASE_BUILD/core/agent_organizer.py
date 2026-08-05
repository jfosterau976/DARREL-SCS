class AgentOrganizer:
    def __init__(self):
        self.name = "Agent Organizer"
        self.agents = {}

    def register(self, name, agent, role, skills=None):
        self.agents[name] = {
            "agent": agent,
            "role": role,
            "skills": skills or [],
            "status": "online"
        }

    def get(self, name):
        return self.agents.get(name)

    def list_agents(self):
        return {
            name: {
                "role": details["role"],
                "skills": details["skills"],
                "status": details["status"]
            }
            for name, details in self.agents.items()
        }

    def health_check(self):
        return {
            name: details["status"]
            for name, details in self.agents.items()
        }


agent_organizer = AgentOrganizer()