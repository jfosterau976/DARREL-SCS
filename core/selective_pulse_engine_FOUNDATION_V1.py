from datetime import datetime
import uuid

from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_engine import synthesis_engine
from core.verifier_engine import verifier_engine
from core.decision_engine import decision_engine
from core.learning_feedback import learning_feedback
from core.cognitive_memory import cognitive_memory


class SelectivePulseEngine:

    def __init__(self):
        self.name = "SCS Selective Pulse Engine"
        self.pulse_count = 0
        self.history = []


    def run(self, question, modules):

        self.pulse_count += 1

        memories = cognitive_memory.recall()
        print("PULSE MEMORY CHECK:", len(memories), memories)
        print("MEMORY TEST:", memories)
        pulse = {
            "pulse_id": str(uuid.uuid4())[:8],
            "pulse_number": self.pulse_count,
            "timestamp": datetime.now().isoformat(),
            "state": "active",
            "question": question,
            "memory_recall": memories
        }


        result = {
            "system": self.name,
            "pulse": pulse,
            "memory_recall": memories,
            "pulse_memory_recall": memories,
            "activated_modules": modules,
            "status": "active"
        }


        left = None
        right = None
        synthesis = None
        verification = None


        if "left_reasoning" in modules:
            left = left_brain.think(
                question,
                memories
        )
            result["left"] = left


        if "right_reasoning" in modules:
            right = right_brain.think(question)
            result["right"] = right


        if "synthesis" in modules and left and right:

            synthesis = synthesis_engine.combine(
                left,
                right,
                question
            )

            result["synthesis"] = synthesis


        if "verifier" in modules and synthesis:

            verification = verifier_engine.verify(
                synthesis
            )

            result["verification"] = verification


        if synthesis and verification:

            decision = decision_engine.decide(
                question,
                synthesis,
                verification
            )

            result["decision"] = decision


        performance = {
            "synthesis": synthesis,
            "verification": verification,
            "decision": result.get("decision")
        }


        learning = learning_feedback.evaluate(
            performance
        )


        result["learning"] = learning


        result["pulse"]["state"] = "complete"

        self.history.append(result)

        result["status"] = "selective_pulse_complete"


        return result



selective_pulse_engine = SelectivePulseEngine()