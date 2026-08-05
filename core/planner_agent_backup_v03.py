from core.cognitive_memory import cognitive_memory


class PlannerAgent:

    def __init__(self):

        self.name = "SCS Planner Agent"


    def create_plan(self, request):

        memories = cognitive_memory.recall()

        relevant = []

        for memory in memories:

            text = str(memory).lower()

            if any(word in text for word in request.lower().split()):

                relevant.append(memory)


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


        return {

            "agent": self.name,

            "status": "plan_created",

            "request": request,

            "memory_matches": len(relevant),

            "relevant_memories": relevant,

            "plan": plan,

            "estimated_steps": len(plan)

        }


planner_agent = PlannerAgent()