from core.cognitive_controller import cognitive_controller
from core.attention_manager import attention_manager
from core.executive_manager import executive_manager
from core.coordinator import coordinator
from agents.memory_agent import memory_agent
from core.tree_router import tree_router
from core.branch_manager import branch_manager
from core.neural_tree_executor import neural_tree_executor



class ThinkingLoop:

    def __init__(self):
        self.name = "SCS Thinking Loop"


    def think(self, request):
        print("\n🧠 THINKING LOOP START")
        print("Input:", request)


        # 0. Select brain branches using Neural Tree
        tree_path = tree_router.route(request)

        print("\n🌳 Active Brain Branches:")
        for branch in tree_path["active_branches"]:
            print("-", branch)
        # Activate tree branches
        branches = branch_manager.activate(
            tree_path["active_branches"]
        )

        print("\n🌳 Branch Activation:")
        print(branches)


        # Prepare execution pathway
        execution = neural_tree_executor.execute(
            branches["activated"]
        )

        print("\n⚡ Tree Execution:")
        print(execution)


        # 1. Recall previous experience
        memory = memory_agent.recall_memories(request)

        print("\nMemory Recall:")
        print(memory)


        # 2. Analyse importance
        attention = attention_manager.analyse_priority(request)

        print("\nAttention:")
        print(attention)


        priorities = attention["priorities"]


        # 3. Decide required skills and agents
        decision = cognitive_controller.think(request)

        skills = decision.get(
            "skills_needed",
            []
        )

        agents = decision.get(
            "agents_selected",
            []
        )


        # 4. Create execution plan
        plan = executive_manager.create_plan(
            skills,
            agents,
            priorities
        )

        print("\nExecution Plan:")
        print(plan)


        # 5. Execute thinking process
        result = coordinator.process(
            request,
            plan
        )


        # 6. Save new experience
        saved = memory_agent.save_memory(
            request,
            result
        )

        print("\nMemory Saved:")
        print(saved)


        return {
            "memory_recall": memory,
            "attention": attention,
            "plan": plan,
            "result": result,
            "memory_saved": saved
        }


thinking_loop = ThinkingLoop()