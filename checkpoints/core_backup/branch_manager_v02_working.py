class BranchManager:

    def __init__(self):

        self.name = "SCS Branch Manager"


        self.branches = {

            "safety": [
                "verifier_agent"
            ],

            "reasoning": [
                "left_brain"
            ],

            "creativity": [
                "right_brain"
            ],

            "knowledge": [
                "research_agent"
            ],

            "memory": [
                "memory_agent",
                "learning_agent",
                "optimizer_agent"
            ]

        }



    def activate(self, branches):

        activated = []


        for item in branches:


            # Old format support
            if isinstance(item, str):

                branch = item
                priority = "medium"
                reason = "Default activation"


            # New neural tree format
            else:

                branch = item["branch"]
                priority = item.get("priority", "medium")
                reason = item.get("reason", "No reason provided")



            if branch in self.branches:


                activated.append({

                    "branch": branch,

                    "priority": priority,

                    "reason": reason,

                    "agents": self.branches[branch]

                })



        return {

            "manager": self.name,

            "status": "branches_activated",

            "activated": activated

        }



branch_manager = BranchManager()