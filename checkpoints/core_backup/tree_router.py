class TreeRouter:

    def __init__(self):

        self.name = "SCS Tree Router"


    def route(self, request, priorities, strategy=None):

        branches = []


        if strategy:

            if strategy.get("verification_priority") == "high":

                branches.append({

                    "branch": "safety",

                    "priority": "high",

                    "reason": "Planner strategy selected verification"

                })


            if strategy.get("research_priority") == "high":

                branches.append({

                    "branch": "knowledge",

                    "priority": "high",

                    "reason": "Planner strategy selected research"

                })


            if strategy.get("reasoning_priority") == "high":

                branches.append({

                    "branch": "reasoning",

                    "priority": "high",

                    "reason": "Planner strategy selected reasoning"

                })


            if strategy.get("creativity_priority") == "high":

                branches.append({

                    "branch": "creativity",

                    "priority": "high",

                    "reason": "Planner strategy selected creativity"

                })


        else:

            branches = [

                {

                    "branch": "reasoning",

                    "priority": "medium",

                    "reason": "Default reasoning branch"

                },

                {

                    "branch": "creativity",

                    "priority": "medium",

                    "reason": "Default creativity branch"

                }

            ]


        return {

            "router": self.name,

            "status": "branches_selected",

            "planner_controlled": bool(strategy),

            "input": request,

            "active_branches": branches

        }


tree_router = TreeRouter()