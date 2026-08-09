import time
from datetime import datetime

from core.pulse import pulse
from core.memory_consolidator import memory_consolidator
from core.reflection_agent import reflection_agent
from core.learning_feedback import learning_feedback
from core.scs_executive import scs_executive


class Coordinator:

    def __init__(self):

        self.name = "SCS Central Coordinator"


    def process(self, question):

        print("\n=== SCS COORDINATOR ===")

        start_time = time.perf_counter()

        started_at = datetime.now().isoformat(
            timespec="seconds"
        )


        # Run Pulse Engine

        pulse_result = pulse.run(question)


        execution = pulse_result.get(
            "execution",
            {}
        )


        results = execution.get(
            "results",
            {}
        )


        activated_modules = pulse_result.get(
            "execution_plan",
            {}
        ).get(
            "modules_to_run",
            []
        )


        # Extract outputs

        left = results.get(
            "left_reasoning",
            {}
        ).get(
            "output",
            {}
        )

        right = results.get(
            "right_reasoning",
            {}
        ).get(
            "output",
            {}
        )

        synthesis = results.get(
            "synthesis",
            {}
        ).get(
            "output",
            {}
        )

        verification = results.get(
            "verifier",
            {}
        ).get(
            "output",
            {}
        )


        reflection = results.get(
            "reflection",
            {}
        ).get(
            "output",
            {}
        )

        learning = results.get(
            "learning",
            {}
        ).get(
            "output",
            {}
        )


        # Respect Pulse decisions

        if (
            "reflection" in activated_modules
            and verification
            and not reflection
        ):

            reflection = reflection_agent.reflect(
                verification
            )


        if (
            "learning" in activated_modules
            and verification
            and not learning
        ):

            learning = learning_feedback.evaluate({

                "synthesis": synthesis,

                "verification": verification,

                "reflection": reflection

            })


        if "memory" in activated_modules:

            memory = memory_consolidator.consolidate()

        else:

            memory = {

                "status": "skipped",

                "reason": "not_required"

            }


        if "executive" in activated_modules:

            executive = scs_executive.process(

                question,

                synthesis,

                verification

            )

        else:

            executive = {

                "status": "skipped",

                "reason": "not_required"

            }



        duration_seconds = round(

            time.perf_counter() - start_time,

            3

        )


        cognitive_state = pulse_result.get(

            "cognitive_state",

            {}

        )


        llm_results = []

        for module_name, module_result in results.items():

            if not isinstance(module_result, dict):
                continue

            module_output = module_result.get(
                "output",
                {}
            )

            if not isinstance(module_output, dict):
                continue

            for llm_key in [
                "llm",
                "revision_llm"
            ]:

                llm_result = module_output.get(
                    llm_key,
                    {}
                )

                if (
                    isinstance(llm_result, dict)
                    and llm_result
                ):

                    llm_results.append({
                        "module": module_name,
                        "call_type": llm_key,
                        "result": llm_result
                    })


        providers = []
        models = []

        input_tokens = 0
        output_tokens = 0

        prompt_tokens = 0
        eval_tokens = 0

        fallback_used = False

        llm_calls = []


        for item in llm_results:

            llm_result = item["result"]

            provider = llm_result.get(
                "provider"
            )

            model = llm_result.get(
                "model"
            )

            status = llm_result.get(
                "status"
            )

            fallback = llm_result.get(
                "fallback",
                False
            )

            requested_provider = llm_result.get(
                "requested_provider"
            )

            actual_provider = llm_result.get(
                "actual_provider"
            ) or provider

            call_fallback_used = llm_result.get(
                "fallback_used",
                fallback
            )

            fallback_reason = llm_result.get(
                "fallback_reason"
            )

            metrics = llm_result.get(
                "metrics",
                {}
            ) or {}

            if (
                provider
                and provider not in providers
            ):
                providers.append(
                    provider
                )

            if (
                model
                and model not in models
            ):
                models.append(
                    model
                )

            if call_fallback_used:
                fallback_used = True

            input_tokens += (
                metrics.get(
                    "input_tokens"
                )
                or 0
            )

            output_tokens += (
                metrics.get(
                    "output_tokens"
                )
                or 0
            )

            prompt_tokens += (
                metrics.get(
                    "prompt_eval_count"
                )
                or 0
            )

            eval_tokens += (
                metrics.get(
                    "eval_count"
                )
                or 0
            )

            llm_calls.append({
                "module": item["module"],
                "call_type": item["call_type"],
                "provider": provider,
                "requested_provider": requested_provider,
                "actual_provider": actual_provider,
                "model": model,
                "status": status,
                "fallback": fallback,
                "fallback_used": call_fallback_used,
                "fallback_reason": fallback_reason,
                "metrics": metrics
             })


        telemetry = {

            "system": {

                "name": self.name,

                "status": "workspace_complete",

                "started_at": started_at,

                "duration_seconds": duration_seconds

            },

            "pulse": {

                "complexity": cognitive_state.get(
                    "complexity"
                ),

                "risk": cognitive_state.get(
                    "risk"
                ),

                "activated_modules": activated_modules,

                "module_count": len(
                    activated_modules
                )

            },

            "llm": {

                "providers": providers,

                "models": models,

                "llm_call_count": len(
                    llm_results
                ),

                "input_tokens": input_tokens,

                "output_tokens": output_tokens,

                "prompt_tokens": prompt_tokens,

                "eval_tokens": eval_tokens,

                "fallback_used": fallback_used,

                "calls": llm_calls

            }

        }


        # Compare the shadow budget with observed execution. This record is
        # diagnostic only and cannot alter routing or execution.

        budget_proposal = pulse_result.get(
            "telemetry",
            {}
        ).get(
            "cognitive_budget",
            {}
        )

        budget_record = budget_proposal or {}

        if budget_proposal.get("status") == "proposed":

            verification_passes = (
                int(bool(execution.get("initial_verification")))
                + int(bool(execution.get("corrected_verification")))
            )

            if (
                verification_passes == 0
                and verification
            ):
                verification_passes = 1

            actual_usage = {
                "latency_ms": round(duration_seconds * 1000, 2),
                "total_tokens": (
                    input_tokens
                    + output_tokens
                    + prompt_tokens
                    + eval_tokens
                ),
                "api_cost": None,
                "model_calls": len(llm_results),
                "memory_lookups": None,
                "tool_calls": None,
                "modules": len(activated_modules),
                "verification_passes": verification_passes,
                "correction_passes": int(bool(
                    execution.get("correction_attempted")
                )),
            }

            try:
                from core.cognitive_budget_manager import (
                    cognitive_budget_manager
                )

                budget_record = cognitive_budget_manager.compare(
                    budget_proposal,
                    actual_usage
                )

            except Exception as error:
                budget_record = {
                    **budget_proposal,
                    "mode": "shadow",
                    "version": "cognitive-budget-v0.1",
                    "status": "error",
                    "authority": False,
                    "enforced": False,
                    "stage": "comparison",
                    "error_type": type(error).__name__,
                    "actual_usage": actual_usage,
                }

        pulse_result.setdefault(
            "telemetry",
            {}
        )["cognitive_budget"] = budget_record

        telemetry["cognitive_budget"] = budget_record


        return {

            "system": self.name,

            "status": "workspace_complete",

            "question": question,

            "pulse": pulse_result,

            "activated_modules": activated_modules,

            "memory": memory,

            "left_brain": left,

            "right_brain": right,

            "synthesis": synthesis,

            "verification": verification,

            "reflection": reflection,

            "learning": learning,

            "executive": executive,

            "telemetry": telemetry

        }


coordinator = Coordinator()
