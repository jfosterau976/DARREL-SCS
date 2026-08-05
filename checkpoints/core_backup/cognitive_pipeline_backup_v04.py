
from core.cognitive_memory import cognitive_memory
from core.attention_manager import attention_manager
from core.tree_router import tree_router
from core.branch_manager import branch_manager
from core.neural_tree_executor import neural_tree_executor
from core.coordinator import coordinator
from core.planner_agent import planner_agent


class CognitivePipeline:

    def __init__(self):

        self.name = "SCS Cognitive Pipeline"


    def run(self, request):

        print("\n🧠 SCS COGNITIVE PIPELINE START")
        print("Input:", request)


        # 1. Planning layer
        plan = planner_agent.create_plan(request)

        print("\n🧭 Planning:")
        print(plan)


        # 2. Memory recall
        memory = cognitive_memory.recall()

        print("\nMemory:")
        print(memory)


        # 3. Attention analysis
        attention = attention_manager.analyse_priority(request)

        print("\nAttention:")
        print(attention)


        # 4. Tree routing controlled by planner
        tree = tree_router.route(
            request,
            attention["priorities"],
            plan
        )

        print("\n🌳 Tree Selection:")
        print(tree)


        # 5. Activate branches
        activated = branch_manager.activate(
            tree["active_branches"]
        )

        print("\n🌿 Branch Activation:")
        print(activated)


        # 6. Execute neural tree
        execution = neural_tree_executor.execute(
            activated["activated"]
        )

        print("\n⚡ Tree Execution:")
        print(execution)


        # 7. Coordinator synthesis
        result = coordinator.process(request)


        return {

            "pipeline": self.name,

            "status": "complete",

            "plan": plan,

            "memory": memory,

            "attention": attention,

            "tree": tree,

            "branches": activated,

            "execution": execution,

            "result": result

        }


cognitive_pipeline = CognitivePipeline()