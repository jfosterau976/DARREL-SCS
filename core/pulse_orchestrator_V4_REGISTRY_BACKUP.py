from core.module_registry_setup import get_registry


class PulseOrchestrator:

    def __init__(self):

        self.name = "SCS Pulse Orchestrator V4"

        self.registry = get_registry()


    def decide_execution(self, activation):

        modules = activation.get(
            "activated_modules",
            []
        )

        return {

            "orchestrator": self.name,

            "modules_to_run": modules,

            "module_count": len(modules),

            "status": "execution_plan_created"

        }


    def execute(self, execution_plan, context):

        results = {}

        modules = execution_plan.get(
            "modules_to_run",
            []
        )


        for module_name in modules:

            module = self.registry.get(
                module_name
            )

            if module is None:

                results[module_name] = {
                    "status": "module_not_found"
                }

                continue


            results[module_name] = {
                "status": "registered",
                "module": str(module)
            }


        return {

            "orchestrator": self.name,

            "executed_modules": modules,

            "results": results,

            "status": "execution_complete"

        }


pulse_orchestrator = PulseOrchestrator()