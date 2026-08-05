from core.cognitive_memory import cognitive_memory


class PlannerAgent:

    def __init__(self):

        self.name = "SCS Planner Agent"


    def select_strategy(self, memories):

        strategy = {

            "verification_priority": "normal",

            "research_priority": "normal",

            "reasoning_priority": "normal",

            "creativity_priority": "normal"

        }


        for item in memories:

            memory = str(item).lower()


            if "review" in memory:

                strategy["verification_priority"] = "high"


            if "multiple agents" in memory:

                strategy["reasoning_priority"] = "high"


            if "planning agent" in memory:

                strategy["research_priority"] = "high"


        return strategy



    def create_plan(self, request):

        relevant_memories = cognitive_memory.recall_relevant(
            request
        )


        strategy = self.select_strategy(
            relevant_memories
        )


        plan = [

            "Recall relevant memories",

            "Analyse request priority",

            "Select adaptive strategy",

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

            "strategy": strategy,

            "agents": agents,

            "plan": plan,

            "estimated_steps": len(plan)

        }


planner_agent = PlannerAgent()