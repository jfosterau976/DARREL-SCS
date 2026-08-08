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
        else:
            question = str(context)
            memories = []

        left_output = None
        right_output = None
        synthesis_output = None
        verification_output = None
        reflection_output = None

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
                    output = module.think(question, memories)
                    left_output = output

                elif module_name == "right_reasoning":
                    output = module.think(question, memories)
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
                        right_output
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

                    output = module.verify(target)
                    verification_output = output

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
                    (time.perf_counter() - module_timer) * 1000,
                    2
                )

                module_times_ms[module_name] = elapsed_ms

        return {
            "orchestrator": self.name,
            "executed_modules": modules,
            "module_times_ms": module_times_ms,
            "results": results,
            "status": "execution_complete"
        }


pulse_orchestrator = PulseOrchestrator()