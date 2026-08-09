from collections.abc import Mapping

from core.attention_router import attention_router
from core.pulse_orchestrator_V3 import pulse_orchestrator
from core.telemetry import telemetry


class Pulse:

    NEURAL_ROUTING_VERSION = "neural-routing-v0.1"

    def __init__(self):

        self.name = "SCS Pulse Engine"
        self.version = "V0.2"

    def shadow_error(self, stage, error):

        return {
            "mode": "shadow",
            "version": self.NEURAL_ROUTING_VERSION,
            "status": "error",
            "authority": False,
            "stage": stage,
            "error_type": type(error).__name__,
        }

    def normalize_shadow_comparison(self, record):
        prefix = "neural_routing.comparison"

        if not isinstance(record, Mapping):
            return {
                "mode": "shadow",
                "version": self.NEURAL_ROUTING_VERSION,
                "status": "error",
                "authority": False,
                "stage": "comparison_contract",
                "data_quality": {
                    "valid": False,
                    "normalized_fields": [prefix],
                },
            }

        normalized_fields = []

        if record.get("mode") != "shadow":
            normalized_fields.append(f"{prefix}.mode")

        if record.get("version") != self.NEURAL_ROUTING_VERSION:
            normalized_fields.append(f"{prefix}.version")

        if record.get("authority") is not False:
            normalized_fields.append(f"{prefix}.authority")

        status = record.get("status")
        if status not in {"compared", "error", "unavailable"}:
            status = "error"
            normalized_fields.append(f"{prefix}.status")

        quality = record.get("data_quality")
        if quality is not None:
            if isinstance(quality, Mapping):
                fields = quality.get("normalized_fields", [])

                if isinstance(fields, (list, tuple)):
                    valid_fields = [
                        item
                        for item in fields
                        if isinstance(item, str) and item
                    ]
                    normalized_fields.extend(valid_fields)

                    if len(valid_fields) != len(fields):
                        normalized_fields.append(
                            f"{prefix}.data_quality.normalized_fields"
                        )
                else:
                    normalized_fields.append(
                        f"{prefix}.data_quality.normalized_fields"
                    )
            else:
                normalized_fields.append(f"{prefix}.data_quality")

        return {
            **record,
            "mode": "shadow",
            "version": self.NEURAL_ROUTING_VERSION,
            "status": status,
            "authority": False,
            "data_quality": {
                "valid": not normalized_fields,
                "normalized_fields": sorted(set(normalized_fields)),
            },
        }

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

        # --------------------------
        # Neural Routing Shadow
        # --------------------------

        neural_layer = None
        shadow_prediction = None
        shadow_failure = None

        t = telemetry.begin_module()

        try:
            from core.neural_routing_layer import neural_routing_layer

            neural_layer = neural_routing_layer
            shadow_prediction = neural_layer.predict(
                question
            )

        except Exception as error:
            shadow_failure = self.shadow_error(
                "prediction",
                error
            )

        telemetry.end_module(
            "neural_routing_shadow",
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
        # Cognitive Budget Shadow
        # --------------------------

        budget_manager = None
        budget_proposal = None

        t = telemetry.begin_module()

        try:
            from core.cognitive_budget_manager import (
                cognitive_budget_manager
            )

            budget_manager = cognitive_budget_manager
            neural_signals = (
                shadow_prediction.get("signals", {})
                if shadow_prediction
                else {}
            )
            budget_proposal = budget_manager.propose(
                question,
                cognitive_state,
                neural_signals
            )

        except Exception as error:
            if budget_manager is not None:
                budget_proposal = budget_manager.error_record(
                    "proposal",
                    error
                )
            else:
                budget_proposal = {
                    "mode": "shadow",
                    "version": "cognitive-budget-v0.1",
                    "status": "error",
                    "authority": False,
                    "enforced": False,
                    "stage": "proposal",
                    "error_type": type(error).__name__,
                }

        telemetry.cognitive_budget = budget_proposal

        telemetry.end_module(
            "cognitive_budget_shadow",
            t
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

        if shadow_prediction is not None:

            try:
                comparison = neural_layer.compare(
                    shadow_prediction,
                    routing,
                    execution
                )
                telemetry.neural_routing = self.normalize_shadow_comparison(
                    comparison
                )

            except Exception as error:
                telemetry.neural_routing = self.shadow_error(
                    "comparison",
                    error
                )

        else:
            telemetry.neural_routing = shadow_failure or {
                "mode": "shadow",
                "version": "neural-routing-v0.1",
                "status": "unavailable",
                "authority": False,
            }

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
