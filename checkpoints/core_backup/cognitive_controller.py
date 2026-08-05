from core.coordinator import coordinator
from core.improvement_memory import improvement_memory
from core.executive_manager import executive_manager


class CognitiveController:

    def __init__(self):
        self.name = "Cognitive Controller"


    def identify_skills(self, message):

        message = message.lower()

        skills = []


        if any(word in message for word in [
            "create",
            "idea",
            "invent",
            "design",
            "new"
        ]):
            skills.append("creativity")


        if any(word in message for word in [
            "analyse",
            "analysis",
            "compare",
            "evaluate",
            "risk",
            "problem"
        ]):
            skills.append("analysis")


        if any(word in message for word in [
            "research",
            "facts",
            "information",
            "latest",
            "evidence"
        ]):
            skills.append("research")


        if any(word in message for word in [
            "verify",
            "check",
            "prove",
            "confirm",
            "safe"
        ]):
            skills.append("verification")


        high_risk_topics = [
            "healthcare",
            "medical",
            "elderly",
            "finance",
            "financial",
            "legal",
            "security",
            "safety"
        ]


        if any(topic in message for topic in high_risk_topics):

            if "analysis" not in skills:
                skills.append("analysis")

            if "verification" not in skills:
                skills.append("verification")

            if "research" not in skills:
                skills.append("research")


        return skills



    def select_agents(self, skills):

        agents = []


        if "creativity" in skills:
            agents.append("right_brain")


        if "analysis" in skills:
            agents.append("left_brain")


        if "research" in skills:
            agents.append("research_agent")


        if "verification" in skills:
            agents.append("verifier_agent")


        return agents



    def think(self, message):

        improvements = improvement_memory.load_memory()

        skills = self.identify_skills(message)

        agents = self.select_agents(skills)


        plan = executive_manager.create_plan(
            skills,
            agents
        )


        results = coordinator.process(message)


        return {
            "controller": self.name,
            "status": "online",
            "message": message,
            "skills_needed": skills,
            "agents_selected": agents,
            "thinking_plan": plan,
            "improvements_available": len(
                improvements.get("improvements", [])
            ),
            "results": results
        }



cognitive_controller = CognitiveController()