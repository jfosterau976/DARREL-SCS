from core.message_bus import message_bus


class NeuralTreeExecutor:

    def __init__(self):

        self.name = "SCS Neural Tree Executor"


    def execute(self, activated_branches):

        execution = []
        messages = []


        for branch in activated_branches:

            branch_result = {

                "branch": branch["branch"],

                "agents": [],

                "status": "branch_activated"

            }


            for agent in branch.get("agents", []):

                agent_status = {

                    "agent": agent,

                    "status": "activated"

                }

                branch_result["agents"].append(agent_status)


            execution.append(branch_result)


        # Agent communication phase

        active_agents = []

        for item in execution:

            for agent in item["agents"]:

                active_agents.append(agent["agent"])


        for sender in active_agents:

            for receiver in active_agents:

                if sender != receiver:

                    result = message_bus.send(
                        sender,
                        receiver,
                        "Coordinate with branch agent",
                        "medium"
                    )

                    messages.append(result)


        return {

            "executor": self.name,

            "status": "tree_execution_active",

            "execution": execution,

            "messages": messages

        }


neural_tree_executor = NeuralTreeExecutor()