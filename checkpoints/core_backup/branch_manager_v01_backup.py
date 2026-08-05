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

        for branch in branches:

            if branch in self.branches:
                activated.append({
                    "branch": branch,
                    "agents": self.branches[branch]
                })


        return {
            "manager": self.name,
            "status": "branches_activated",
            "activated": activated
        }


branch_manager = BranchManager()