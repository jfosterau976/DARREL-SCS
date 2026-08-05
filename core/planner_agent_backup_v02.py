class PlannerAgent:

    def __init__(self):

        self.name = "SCS Planner Agent"


    def create_plan(self, request):

        agents = []

        request_lower = request.lower()


        # Reasoning always available
        agents.append("left_brain")


        # Creativity detection
        if any(word in request_lower for word in [
            "create",
            "design",
            "build",
            "idea",
            "invent"
        ]):
            agents.append("right_brain")


        # Research / knowledge detection
        if any(word in request_lower for word in [
            "research",
            "medical",
            "health",
            "science",
            "facts",
            "data"
        ]):
            agents.append("research_agent")


        # Safety detection
        if any(word in request_lower for word in [
            "safe",
            "safety",
            "risk",
            "healthcare",
            "medical"
        ]):
            agents.append("verifier_agent")


        # Memory activation
        if any(word in request_lower for word in [
            "remember",
            "previous",
            "learned",
            "history",
            "past"
        ]):
            agents.append("memory_agent")


        return {

            "agent": self.name,

            "status": "plan_created",

            "request": request,

            "agents": agents,

            "plan": [
                "Recall relevant memories",
                "Analyse request priority",
                "Select cognitive branches",
                "Activate specialist agents",
                "Execute reasoning tree",
                "Synthesize agent outputs",
                "Verify final response",
                "Learn from outcome"
            ],

            "estimated_steps": 8

        }


planner_agent = PlannerAgent()