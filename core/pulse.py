from core.attention_router import attention_router
from core.pulse_orchestrator_V3 import pulse_orchestrator
from core.telemetry import telemetry


class Pulse:

    def __init__(self):

        self.name = "SCS Pulse Engine"
        self.version = "V0.2"

    def run(self, question):

        telemetry.start(question)

        # --------------------------
        # Attention Router
        # --------------------------

        t = telemetry.begin_module()

        routing = attention_router.route(
            question
        )

        telemetry.end_module(
            "attention_router",
            t
        )

        cognitive_state = routing.get(
            "cognitive_state",
            {}
        )

        activation = routing.get(
            "activation",
            {}
        )

        # --------------------------
        # Execution Planning
        # --------------------------

        t = telemetry.begin_module()

        execution_plan = pulse_orchestrator.decide_execution(
            activation
        )

        telemetry.end_module(
            "execution_plan",
            t
        )

        # --------------------------
        # Execute Modules
        # --------------------------

        t = telemetry.begin_module()

        execution_context = {
            "question": question,
            "complexity": routing.get(
                "cognitive_state",
                {}
            ).get(
                "complexity",
                "medium"
            )
        }

        execution = pulse_orchestrator.execute(
            execution_plan,
            execution_context
        )

        telemetry.end_module(
            "cognitive_execution",
            t
        )

        # --------------------------
        # Collect Statistics
        # --------------------------

        results = execution.get(
            "results",
            {}
        )

        telemetry.memory_count = len(
            results.get(
                "memory",
                {}
            ).get(
                "output",
                []
            )
        )

        telemetry.verification_confidence = (
            results.get(
                "verifier",
                {}
            ).get(
                "output",
                {}
            ).get(
                "confidence",
                0
            )
        )

        telemetry.executive_confidence = (
            results.get(
                "executive",
                {}
            ).get(
                "output",
                {}
            ).get(
                "confidence",
                0
            )
        )

        left = (
            results.get(
                "left_reasoning",
                {}
            ).get(
                "output",
                {}
            )
        )

        if "llm" in left:

            telemetry.llm = (
                left["llm"].get(
                    "model",
                    ""
                )
            )

        telemetry.finish()

        return {

            "system": self.name,

            "version": self.version,

            "question": question,

            "routing": routing,

            "cognitive_state": cognitive_state,

            "activation": activation,

            "execution_plan": execution_plan,

            "execution": execution,

            "telemetry": telemetry.export(),

            "status": "pulse_complete"

        }


pulse = Pulse()