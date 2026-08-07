from core.pulse_orchestrator_V3 import pulse_orchestrator as dynamic_orchestrator


class PulseOrchestrator:

    def __init__(self):
        self.name = "SCS Pulse Orchestrator"

    def run_pulse(self, activation, context):

        execution_plan = dynamic_orchestrator.decide_execution(
            activation
        )

        result = dynamic_orchestrator.execute(
            execution_plan,
            context
        )

        return {
            "system": self.name,
            "execution_plan": execution_plan,
            "result": result,
            "status": "pulse_complete"
        }


pulse_orchestrator = PulseOrchestrator()