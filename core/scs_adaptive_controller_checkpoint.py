from core.pulse_intelligence_router import pulse_router
from core.strategy_evolution_engine import strategy_evolution_engine
from core.cognitive_pulse_v1 import cognitive_pulse
from core.adaptive_learning_loop import adaptive_learning_loop


class SCSAdaptiveController:

    def __init__(self):
        self.name = "SCS Adaptive Controller"


    def process(self, question):

        route = pulse_router.route(question)

        strategy = strategy_evolution_engine.evolve(
            question
        )

        pulse = cognitive_pulse.run(
            question
        )

        learning = adaptive_learning_loop.learn(
            question,
            pulse
        )

        return {
            "system": self.name,
            "route": route,
            "strategy": strategy,
            "pulse": pulse,
            "learning": learning,
            "status": "adaptive_complete"
        }


scs_adaptive_controller = SCSAdaptiveController()