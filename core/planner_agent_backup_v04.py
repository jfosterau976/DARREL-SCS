from core.cognitive_memory import cognitive_memory


class PlannerAgent:

    def __init__(self):

        self.name = "SCS Planner Agent"


    def create_plan(self, request):

        relevant_memories = cognitive_memory.recall_relevant(
            request
        )


        plan = [

            "Recall relevant memories",

            "Analyse request priority",

            "Select cognitive branches",

            "Activate specialist agents",

            "Execute reasoning tree",

            "Synthesize agent outputs",

            "Verify final response",

            "Learn from outcome"

        ]


        agents = [

            "left_brain",

            "right_brain",

            "research_agent",

            "verifier_agent"

        ]


        return {

            "agent": self.name,

            "status": "plan_created",

            "request": request,

            "memory_matches": len(relevant_memories),

            "memory_context": relevant_memories,

            "agents": agents,

            "plan": plan,

            "estimated_steps": len(plan)

        }


planner_agent = PlannerAgent()