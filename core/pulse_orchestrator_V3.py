import time

from core.module_registry_setup import get_registry


class PulseOrchestrator:

    def __init__(self):
        self.name = "SCS Pulse Orchestrator V4"
        self.registry = get_registry()

    def decide_execution(self, activation):

        modules = activation.get("activated_modules", [])

        return {
            "orchestrator": self.name,
            "modules_to_run": modules,
            "module_count": len(modules),
            "status": "execution_plan_created"
        }

    def execute(self, execution_plan, context):

        modules = execution_plan.get("modules_to_run", [])
        results = {}
        module_times_ms = {}

        if isinstance(context, dict):
            question = context.get("question", "")
            memories = context.get("memories", [])
            complexity = context.get("complexity", "medium")
        else:
            question = str(context)
            memories = []
            complexity = "medium"

        if complexity == "low":
            reasoning_think_mode = False
            synthesis_think_mode = False

        elif complexity == "medium":
            reasoning_think_mode = False
            synthesis_think_mode = None

        else:
            reasoning_think_mode = None
            synthesis_think_mode = None

        left_output = None
        right_output = None
        synthesis_output = None
        verification_output = None
        reflection_output = None

        correction_attempted = False
        initial_verification = None
        corrected_verification = None
        verifier_only_elapsed_ms = 0.0

        for module_name in modules:

            module = self.registry.get(module_name)

            if module is None:
                results[module_name] = {
                    "status": "module_not_found"
                }
                continue

            module_timer = time.perf_counter()

            try:

                if module_name == "goal_planning":
                    output = module.think(question)

                elif module_name == "left_reasoning":
                    output = module.think(
                        question,
                        memories,
                        think=reasoning_think_mode
                    )

                    left_output = output

                elif module_name == "right_reasoning":
                    output = module.think(
                        question,
                        memories,
                        think=reasoning_think_mode
                    )

                    right_output = output

                elif module_name == "synthesis":

                    if left_output is None or right_output is None:
                        results[module_name] = {
                            "status": "dependency_missing"
                        }
                        continue

                    output = module.synthesize(
                        question,
                        left_output,
                        right_output,
                        think=synthesis_think_mode
                    )

                    synthesis_output = output

                elif module_name == "verifier":

                    target = (
                        synthesis_output
                        or right_output
                        or left_output
                    )

                    if target is None:
                        results[module_name] = {
                            "status": "dependency_missing"
                        }
                        continue

                    verification_timer = time.perf_counter()
            
                    output = module.verify(target)
            
                    verifier_only_elapsed_ms += round(
                        (
                            time.perf_counter()
                            - verification_timer
                        ) * 1000,
                        2
                    )

                    initial_verification = output
                    verification_output = output

                    if (
                        output.get("verdict") == "REVIEW"
                        and synthesis_output is not None
                        and not correction_attempted
                    ):

                        correction_attempted = True

                        synthesis_module = self.registry.get(
                            "synthesis"
                        )

                        if (
                            synthesis_module is not None
                            and hasattr(
                                synthesis_module,
                                "revise"
                            )
                        ):

                            correction_timer = time.perf_counter()

                            revised_synthesis = (
                                synthesis_module.revise(
                                    question,
                                    synthesis_output,
                                    output,
                                    think=synthesis_think_mode
                                )
                            )

                            correction_elapsed_ms = round(
                                (
                                    time.perf_counter()
                                    - correction_timer
                                ) * 1000,
                                2
                            )

                            module_times_ms[
                                "corrective_revision"
                            ] = correction_elapsed_ms

                            synthesis_output = revised_synthesis

                            if "synthesis" in results:
                                results[
                                    "synthesis"
                                ]["output"] = revised_synthesis

                            verification_timer = time.perf_counter()


                            corrected_verification = (
                                module.verify(
                                    revised_synthesis
                                )
                            )

                            verifier_only_elapsed_ms += round(
                                (
                                    time.perf_counter()
                                    - verification_timer
                                ) * 1000,
                                2
                            )

                            verification_output = (
                                corrected_verification
                            )

                            output = corrected_verification

                elif module_name == "reflection":

                    if verification_output is None:
                        results[module_name] = {
                            "status": "dependency_missing"
                        }
                        continue

                    output = module.reflect(
                        verification_output
                    )

                    reflection_output = output

                elif module_name == "learning":

                    if reflection_output is None:
                        results[module_name] = {
                            "status": "dependency_missing"
                        }
                        continue

                    output = module.extract(
                        reflection_output
                    )

                else:
                    output = {
                        "status": "unknown_execution_method"
                    }

                results[module_name] = {
                    "status": "executed",
                    "output": output
                }

            except Exception as error:

                results[module_name] = {
                    "status": "execution_error",
                    "error": str(error)
                }

            finally:

                elapsed_ms = round(
                    (
                        time.perf_counter()
                        - module_timer
                    ) * 1000,
                    2
                )

                if module_name == "verifier":
                    module_times_ms[module_name] = (
                        verifier_only_elapsed_ms
                    )
                else:
                    module_times_ms[module_name] = elapsed_ms

        return {
            "orchestrator": self.name,
            "executed_modules": modules,
            "module_times_ms": module_times_ms,
            "results": results,
            "complexity": complexity,
            "reasoning_think_mode": reasoning_think_mode,
            "synthesis_think_mode": synthesis_think_mode,
            "correction_attempted": correction_attempted,
            "initial_verification": initial_verification,
            "corrected_verification": corrected_verification,
            "status": "execution_complete"
        }


pulse_orchestrator = PulseOrchestrator()
