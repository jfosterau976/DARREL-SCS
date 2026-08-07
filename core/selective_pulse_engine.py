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

    def select_modules(self, question):

        question = question.lower()

        modules = [
            "left_reasoning",
            "verifier"
        ]

        complex_words = [
            "design",
            "create",
            "build",
            "invent",
            "future",
            "strategy",
            "compare",
            "commercial"
        ]

        if any(word in question for word in complex_words):
            modules.extend([
                "right_reasoning",
                "synthesis",
                "learning"
            ])

        return modules

    def run(self, question):

        self.pulse_count += 1

        modules = self.select_modules(question)

        memories = cognitive_memory.recall()

        pulse = {
            "pulse_id": str(uuid.uuid4())[:8],
            "pulse_number": self.pulse_count,
            "timestamp": datetime.now().isoformat(),
            "state": "active",
            "question": question,
            "modules": modules
        }

        result = {
            "system": self.name,
            "pulse": pulse,
            "activated_modules": modules,
            "memory_recall": memories
        }

        left = None
        right = None
        synthesis = None
        verification = None

        if "left_reasoning" in modules:
            left = left_brain.think(question, memories)
            result["left"] = left

        if "right_reasoning" in modules:
            right = right_brain.think(question)
            result["right"] = right

        if "synthesis" in modules and left and right:
            synthesis = synthesis_engine.combine(left, right, question)
            result["synthesis"] = synthesis

        if "verifier" in modules:

            target = synthesis if synthesis else left

            verification = verifier_engine.verify(target)

            result["verification"] = verification

        if synthesis and verification:
            result["decision"] = decision_engine.decide(
                question,
                synthesis,
                verification
            )

        result["learning"] = learning_feedback.evaluate({
            "synthesis": synthesis,
            "verification": verification,
            "decision": result.get("decision")
        })

        result["pulse"]["state"] = "complete"

        self.history.append(result)

        return result


selective_pulse_engine = SelectivePulseEngine()