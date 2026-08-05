from core.attention_router import attention_router
from core.pulse_orchestrator import pulse_orchestrator
from core.pulse import pulse_controller


class CognitivePulseController:

    def __init__(self):

        self.name = "SCS Cognitive Pulse Controller V1"


    def run(self, question, feedback=None):

        print("\n🧠 SCS COGNITIVE PULSE ACTIVE")

        print(
            "INPUT:",
            question
        )


        # 1. Attention decides what matters
        attention = attention_router.route(
            question
        )


        activation = attention.get(
            "activation",
            {}
        )


        # 2. Pulse selects active modules
        pulse_state = pulse_orchestrator.run_pulse(
            activation
        )


        # 3. Existing pulse controller executes reasoning
        result = pulse_controller.run(
            question,
            feedback
        )


        return {
            "system": self.name,
            "attention": attention,
            "activation": activation,
            "pulse_state": pulse_state,
            "cognitive_result": result,
            "status": "cognitive_pulse_complete"
        }


cognitive_pulse_controller = CognitivePulseController()