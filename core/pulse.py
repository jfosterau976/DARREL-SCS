from core.attention_router import attention_router
from core.pulse_orchestrator_V3 import pulse_orchestrator


class Pulse:

    def __init__(self):

        self.name = "SCS Pulse Engine"
        self.version = "V0.2"

    def run(self, question):

        routing = attention_router.route(
            question
        )

        cognitive_state = routing.get(
            "cognitive_state",
            {}
        )

        activation = routing.get(
            "activation",
            {}
        )

        execution_plan = pulse_orchestrator.decide_execution(
            activation
        )

        execution = pulse_orchestrator.execute(
            execution_plan,
            question
        )

        return {

            "system": self.name,

            "version": self.version,

            "question": question,

            "routing": routing,

            "cognitive_state": cognitive_state,

            "activation": activation,

            "execution_plan": execution_plan,

            "execution": execution,

            "status": "pulse_complete"

        }


pulse = Pulse()