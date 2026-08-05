class TreeRouter:

    def __init__(self):
        self.name = "SCS Tree Router"


    def route(self, request, priorities, plan=None):

        active_branches = []


        # If planner exists, use planner intelligence
        if plan and "agents" in plan:

            agents = plan["agents"]


            if "verifier_agent" in agents:
                active_branches.append({
                    "branch": "safety",
                    "priority": "high",
                    "reason": "Planner selected verification"
                })


            if "research_agent" in agents:
                active_branches.append({
                    "branch": "knowledge",
                    "priority": "high",
                    "reason": "Planner selected research"
                })


            if "right_brain" in agents:
                active_branches.append({
                    "branch": "creativity",
                    "priority": "medium",
                    "reason": "Planner selected creativity"
                })


            if "left_brain" in agents:
                active_branches.append({
                    "branch": "reasoning",
                    "priority": "medium",
                    "reason": "Planner selected reasoning"
                })


        else:

            # fallback mode
            for priority in priorities:

                active_branches.append({
                    "branch": priority["area"],
                    "priority": priority["priority"],
                    "reason": priority["reason"]
                })


        return {

            "router": self.name,

            "status": "branches_selected",

            "planner_controlled": plan is not None,

            "input": request,

            "active_branches": active_branches

        }


tree_router = TreeRouter()