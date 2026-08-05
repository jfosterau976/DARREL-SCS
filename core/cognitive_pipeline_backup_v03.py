from core.cognitive_memory import cognitive_memory
from core.attention_manager import attention_manager
from core.tree_router import tree_router
from core.branch_manager import branch_manager
from core.neural_tree_executor import neural_tree_executor
from core.coordinator import coordinator
from core.synthesis_agent import synthesis_agent


class CognitivePipeline:

    def __init__(self):

        self.name = "SCS Cognitive Pipeline"


    def run(self, request):

        print("\n🧠 SCS COGNITIVE PIPELINE START")
        print("Input:", request)


        # 1. Memory recall
        memory = cognitive_memory.recall()

        print("\nMemory:")
        print(memory)


        # 2. Attention analysis
        attention = attention_manager.analyse_priority(request)

        print("\nAttention:")
        print(attention)


        # 3. Select branches
        tree = tree_router.route(
            request,
            attention["priorities"]
        )

        print("\n🌳 Tree Selection:")
        print(tree)


        # 4. Activate branches
        activated = branch_manager.activate(
            tree["active_branches"]
        )

        print("\n🌿 Branch Activation:")
        print(activated)


        # 5. Execute tree
        execution = neural_tree_executor.execute(
            activated["activated"]
        )

        print("\n⚡ Tree Execution:")
        print(execution)


        # 6. Existing coordinator processing
        result = coordinator.process(request)


        # 7. Synthesis - combine agent outputs
        synthesis = synthesis_agent.synthesize(
            list(result["agent_results"].values())
        )

        print("\n🧩 Synthesis:")
        print(synthesis)

        return {

            "pipeline": self.name,

            "status": "complete",

            "memory": memory,

            "attention": attention,

            "tree": tree,

            "branches": activated,

            "execution": execution,

            "result": result,

            "synthesis": synthesis

        }



cognitive_pipeline = CognitivePipeline()