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


        for branch in branches:

            agents = branch.get(
                "agents",
                []
            )


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


            # Create neural communication signals

            for sender in agents:

                for receiver in agents:

                    if sender != receiver:

                        message = message_bus.send(

                            sender,

                            receiver,

                            "Coordinate with branch agent",

                            priority="medium",

                            confidence=0.8

                        )

                        messages.append(message)



        return {

            "executor": self.name,

            "status": "tree_execution_active",

            "execution": execution,

            "messages": messages

        }



neural_tree_executor = NeuralTreeExecutor()