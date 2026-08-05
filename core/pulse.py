from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_agent import synthesis_agent
from core.verifier_engine import verifier_engine
from core.pulse_router import pulse_router
from core.attention_router import attention_router
from core.reflection_agent import reflection_agent
from core.learning_extractor import learning_extractor
from core.cognitive_memory import cognitive_memory


class PulseController:

    def __init__(self):
        self.name = "SCS Pulse Controller"
        self.version = "V0.5"

    def run(self, question, feedback=None):

        print("\n=== SCS PULSE ===")
        print("Question:", question)
      
        memory_context = cognitive_memory.recall_relevant(
            question
        )

        memory_context_package = {
            "relevant_memories": memory_context,
            "memory_count": len(memory_context),
            "source": "SCS Cognitive Memory"
        }

        print("\nMEMORY CONTEXT:")
        print(f"Relevant memories: {len(memory_context)}")

        for item in memory_context[:3]:
            memory = item.get("memory", {})

            summary = (
                memory.get("question")
                or memory.get("input")
                or memory.get("lesson")
                or memory.get("type")
                or str(memory)[:80]
            )

            print("-", item.get("score"), summary)
        if feedback:
            print("\nFEEDBACK RECEIVED:")
            print(feedback)

        attention_result = attention_router.route(
            question
        )

        decision = {
            "left": "left_reasoning" in attention_result["activation"]["activated_modules"],
             "right": "right_reasoning" in attention_result["activation"]["activated_modules"],
             "synthesis": "synthesis" in attention_result["activation"]["activated_modules"],
             "verifier": "verifier" in attention_result["activation"]["activated_modules"]
        }

        print("\nROUTER DECISION:")
        print(decision)
        print("\nATTENTION STATE:")
        print(attention_result)

        left_result = None
        right_result = None
        synthesis_result = None
        verification_result = None

        # LEFT BRAIN
        if decision["left"]:

            print("\n[LEFT BRAIN] ACTIVE")

            if feedback:
                left_question = (
                    f"{question}\n\n"
                    f"VERIFIER FEEDBACK:\n{feedback}\n\n"
                    "Revise your analysis specifically "
                    "to address this feedback."
                )
            else:
                left_question = question

            left_result = left_brain.think(
                left_question
            )

        # RIGHT BRAIN
        if decision["right"]:

            print("\n[RIGHT BRAIN] ACTIVE")

            if feedback:
                right_question = (
                    f"{question}\n\n"
                    f"VERIFIER FEEDBACK:\n{feedback}\n\n"
                    "Revise your exploration specifically "
                    "to address this feedback."
                )
            else:
                right_question = question

            right_result = right_brain.think(
                right_question
            )

        # SYNTHESIS
        if decision["synthesis"]:

            print("\n[SYNTHESIS] ACTIVE")

            if left_result is None:
                left_result = left_brain.think(question)

            if right_result is None:
                right_result = right_brain.think(question)

            synthesis_result = synthesis_agent.synthesize(
                question,
                left_result,
                right_result
            )

        # VERIFICATION
        if decision["verifier"]:

            print("\n[VERIFIER] ACTIVE")

            target_result = (
                synthesis_result
                or right_result
                or left_result
            )

            if target_result is not None:

                verification_result = verifier_engine.verify(
                    target_result
                )
                reflection_result = None

           
            if verification_result:

                   print("\n[REFLECTION] ACTIVE")

                   reflection_result = reflection_agent.reflect(
                       verification_result
                )
                   learning_result = learning_extractor.extract(
                       reflection_result
            )
                   memory_result = cognitive_memory.remember(
                       learning_result
            )
        return {
            "question": question,
            "decision": decision,

            "left_brain": (
                left_result
                if hasattr(left_result, "to_dict")
                else left_result
            ),

            "right_brain": (
                right_result
                if hasattr(right_result, "to_dict")
                else right_result
            ),

            "synthesis": (
                synthesis_result
                if hasattr(synthesis_result, "to_dict")
                else synthesis_result
            ),

            "verification": (
                verification_result
                if verification_result
                else None
            ),

            "reflection": reflection_result,

            "learning": learning_result, 
        }


pulse_controller = PulseController()