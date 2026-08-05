from core.pulse_intelligence_router import pulse_router
from core.strategy_evolution_engine import strategy_evolution_engine
from core.selective_pulse_engine import selective_pulse_engine
from core.adaptive_learning_loop import adaptive_learning_loop


class UnifiedSCSPulse:

    def __init__(self):
        self.name = "SCS Unified Brain Pulse"


    def think(self, question):

        route = pulse_router.route(question)

        strategy = strategy_evolution_engine.evolve(
            question
        )

        pulse = selective_pulse_engine.run(
            question,
            route["activated_modules"]
        )

        learning = adaptive_learning_loop.learn(
            question,
            pulse
        )

        return {
            "system": self.name,
            "question": question,
            "route": route,
            "strategy": strategy,
            "pulse": pulse,
            "learning": learning,
            "status": "unified_pulse_complete"
        }


scs = UnifiedSCSPulse()