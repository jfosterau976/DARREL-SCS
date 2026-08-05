from core.message_bus import message_bus


class NeuralTreeExecutor:

    def __init__(self):

        self.name = "SCS Neural Tree Executor"


    def execute(self, branches):

        if isinstance(branches, dict):

            branches = branches.get(
                "activated",
                []
            )


        execution = []

        messages = []


        all_agents = []


        for branch in branches:

            agents = branch.get(
                "agents",
                []
            )

            all_agents.extend(agents)


            execution.append({

                "branch": branch["branch"],

                "agents": [

                    {
                        "agent": agent,
                        "status": "activated"
                    }

                    for agent in agents

                ],

                "status": "branch_activated"

            })


        # Cross-branch communication

        for sender in all_agents:

            for receiver in all_agents:

                if sender != receiver:

                    packet = message_bus.send(

                        sender,

                        receiver,

                        "Share findings and coordinate reasoning",

                        priority="medium",

                        confidence=0.8

                    )

                    messages.append(packet)



        return {

            "executor": self.name,

            "status": "tree_execution_active",

            "execution": execution,

            "messages": messages

        }



neural_tree_executor = NeuralTreeExecutor()