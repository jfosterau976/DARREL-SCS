class PlanningAgent:
    def __init__(self):
        self.name = "Planning Agent"
        self.role = "planning"

    def run(self, message):
        return {
            "agent": self.name,
            "role": self.role,
            "input": message,
            "status": "ready"
        }


planning_agent = PlanningAgent()