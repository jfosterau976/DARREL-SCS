from core.decision_router import decision_router
from core.skill_manager import skill_manager
from core.coordinator import coordinator


class CognitiveController:
    def __init__(self):
        self.name = "Cognitive Controller"
        self.status = "online"

    def think(self, message):
        decision = decision_router.decide(message)

        skills = decision["skills_needed"]

        agents = []

        for skill in skills:
            found = skill_manager.find_agents(skill)
            agents.extend(found)

        agents = list(set(agents))

        results = coordinator.process(
            message,
            targets=agents
        )

        return {
            "controller": self.name,
            "status": self.status,
            "message": message,
            "skills_needed": skills,
            "agents_selected": agents,
            "results": results
        }


cognitive_controller = CognitiveController()