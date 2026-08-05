class TreeRouter:

    def __init__(self):
        self.name = "SCS Tree Router"


    def route(self, message, priorities=None):

        text = message.lower()

        branches = []


        # Use attention priorities if available
        if priorities:

            for item in priorities:

                area = item["area"]
                priority = item["priority"]

                if area == "safety":
                    branches.append({
                        "branch": "safety",
                        "priority": priority,
                        "reason": item["reason"]
                    })


                if area == "accuracy":
                    branches.append({
                        "branch": "knowledge",
                        "priority": priority,
                        "reason": item["reason"]
                    })


                if area == "creativity":
                    branches.append({
                        "branch": "creativity",
                        "priority": priority,
                        "reason": item["reason"]
                    })


        # Fallback keyword intelligence
        if "research" in text or "data" in text:
            branches.append({
                "branch": "knowledge",
                "priority": "medium",
                "reason": "Information gathering required"
            })


        if "create" in text or "design" in text or "invent" in text:
            branches.append({
                "branch": "creativity",
                "priority": "medium",
                "reason": "New ideas required"
            })


        # Reasoning always active
        branches.append({
            "branch": "reasoning",
            "priority": "medium",
            "reason": "Logical processing required"
        })


        # Memory always checks experience
        branches.append({
            "branch": "memory",
            "priority": "low",
            "reason": "Previous knowledge retrieval"
        })


        return {
            "router": self.name,
            "status": "branches_selected",
            "input": message,
            "active_branches": branches
        }



tree_router = TreeRouter()