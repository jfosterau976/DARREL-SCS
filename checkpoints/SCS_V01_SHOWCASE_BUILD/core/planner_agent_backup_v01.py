
class PlannerAgent:

    def __init__(self):

        self.name = "SCS Planner Agent"


    def create_plan(self, request):

        agents = []


        request_lower = request.lower()


        # Core reasoning agents
        agents.append("left_brain")
        agents.append("right_brain")


        # Add research when knowledge is needed
        if any(word in request_lower for word in [
            "health",
            "medical",
            "research",
            "information",
            "safer"
        ]):

            agents.append("research_agent")


        # Add verification for safety critical tasks
        if any(word in request_lower for word in [
            "health",
            "medical",
            "safety",
            "secure",
            "risk"
        ]):

            agents.append("verifier_agent")


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