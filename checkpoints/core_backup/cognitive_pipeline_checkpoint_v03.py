from core.planner_agent import planner_agent
from core.tree_router import tree_router
from core.branch_manager import branch_manager
from core.neural_tree_executor import neural_tree_executor
from core.learning_feedback import learning_feedback


class CognitivePipeline:

    def __init__(self):

        self.name = "SCS Cognitive Pipeline"


    def run(self, request):

        print("\n🧠 SCS Cognitive Pipeline Active")


        # 1. Planner creates adaptive plan

        plan = planner_agent.create_plan(request)


        print("\n🧭 Planning:")
        print(plan)


        # 2. Planner strategy controls tree

        tree = tree_router.route(

            request,

            [],

            plan["strategy"]

        )


        print("\n🌳 Tree Selection:")
        print(tree)


        # 3. Activate selected branches

        branches = branch_manager.activate(

            tree["active_branches"]

        )


        print("\n🌿 Branch Activation:")
        print(branches)


        # 4. Execute cognitive tree

        execution = neural_tree_executor.execute(

            branches

        )


        print("\n⚡ Tree Execution:")
        print(execution)


        # 5. Learn from result

        feedback = learning_feedback.evaluate({

            "synthesis": True,

            "verification": True,

            "execution": True

        })


        print("\n📈 Learning Feedback:")
        print(feedback)


        return {

            "planner": plan,

            "tree": tree,

            "branches": branches,

            "execution": execution,

            "feedback": feedback

        }


cognitive_pipeline = CognitivePipeline()