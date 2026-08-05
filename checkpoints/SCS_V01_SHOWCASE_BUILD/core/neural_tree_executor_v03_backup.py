from core.agent_message_router import agent_message_router


class NeuralTreeExecutor:

    def __init__(self):

        self.name = "SCS Neural Tree Executor"

        self.router = agent_message_router

        self.agent_registry = {
            "left_brain": "Left Brain Analysis Agent",
            "right_brain": "Right Brain Model",
            "verifier_agent": "SCS Verifier Agent",
            "research_agent": "Research Agent",
            "memory_agent": "SCS Memory Agent",
            "learning_agent": "Learning Agent",
            "optimizer_agent": "Optimizer Agent"
        }


    def execute(self, activated_branches):

        execution = []
        messages = []


        for branch in activated_branches:

            agents_ready = []

            for agent in branch["agents"]:

                if agent in self.agent_registry:

                    agents_ready.append({
                        "agent": agent,
                        "name": self.agent_registry[agent],
                        "status": "activated"
                    })

                else:

                    agents_ready.append({
                        "agent": agent,
                        "status": "unknown_agent"
                    })


            # Agent communication inside branch
            if len(agents_ready) > 1:

                for sender in agents_ready:

                    for receiver in agents_ready:

                        if sender["agent"] != receiver["agent"]:

                            messages.append(
                                self.router.route(
                                    sender["agent"],
                                    receiver["agent"],
                                    "Coordinate with branch agent",
                                    "medium"
                                )
                            )


            execution.append({

                "branch": branch["branch"],
                "agents": agents_ready,
                "status": "branch_activated"

            })


        return {

            "executor": self.name,
            "status": "tree_execution_active",
            "execution": execution,
            "messages": messages

        }



neural_tree_executor = NeuralTreeExecutor()