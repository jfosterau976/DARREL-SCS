class TreeRouter:

    def __init__(self):

        self.name = "SCS Tree Router"


    def route(self, request, priorities, plan=None):

        branches = []


        # Use planner guidance if available
        planned_agents = []

        if plan:

            planned_agents = plan.get(
                "agents",
                []
            )


        # Safety branch
        if (
            any(
                p["area"] == "safety"
                for p in priorities
            )
            or "verifier_agent" in planned_agents
        ):

            branches.append({

                "branch": "safety",

                "priority": "high",

                "reason":
                "Safety analysis required."

            })


        # Knowledge branch
        if (
            "research_agent" in planned_agents
            or any(
                p["area"] == "accuracy"
                for p in priorities
            )
        ):

            branches.append({

                "branch": "knowledge",

                "priority": "high",

                "reason":
                "Information verification required."

            })


        # Creativity branch
        if (
            "right_brain" in planned_agents
            or any(
                p["area"] == "creativity"
                for p in priorities
            )
        ):

            branches.append({

                "branch": "creativity",

                "priority": "medium",

                "reason":
                "Creative solution generation required."

            })


        # Reasoning branch
        if (
            "left_brain" in planned_agents
        ):

            branches.append({

                "branch": "reasoning",

                "priority": "medium",

                "reason":
                "Logical analysis required."

            })


        # Memory branch always available
        branches.append({

            "branch": "memory",

            "priority": "low",

            "reason":
            "Previous knowledge retrieval."

        })


        return {

            "router": self.name,

            "status": "branches_selected",

            "input": request,

            "planner_controlled": bool(plan),

            "active_branches": branches

        }


tree_router = TreeRouter()