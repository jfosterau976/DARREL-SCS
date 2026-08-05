class AgentOrganizer:
    def __init__(self):
        self.name = "Agent Organizer"
        self.agents = {}

    def register(self, name, role):
        self.agents[name] = {
            "role": role,
            "status": "available"
        }

    def list_agents(self):
        return self.agents


agent_organizer = AgentOrganizer()