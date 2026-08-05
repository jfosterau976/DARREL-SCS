from core.cognitive_state_manager import cognitive_state
from core.cognitive_regulation_engine import cognitive_regulation
from core.pulse_intelligence_router import pulse_router
from core.selective_pulse_engine import selective_pulse_engine
from core.adaptive_learning_loop import adaptive_learning_loop
from core.experience_replay_engine import experience_replay
from core.experience_strategy_selector import experience_strategy_selector


class SelfManagingSCS:

    def __init__(self):
        self.name = "SCS Self Managing Cognitive System"


    def think(self, question):

        # Recall previous experiences
        recalled = experience_replay.recall(
            question
        )

        # Choose strategy from experience
        strategy_choice = experience_strategy_selector.select(
            recalled["matches"]
        )

        # Understand current cognitive state
        state = cognitive_state.evaluate(
            question,
            0.5
        )

        # Regulate thinking effort
        regulation = cognitive_regulation.regulate(
            state
        )

        # Route cognitive modules
        route = pulse_router.route(
            question
        )

        # Run cognitive pulse
        pulse = selective_pulse_engine.run(
            question,
            route["activated_modules"]
        )

        # Learn from result
        learning = adaptive_learning_loop.learn(
            question,
            pulse
        )

        # Store new experience
        experience = experience_replay.store({
            "question": question,
            "strategy": strategy_choice["strategy"],
            "status": "completed"
        })


        return {
            "system": self.name,
            "recalled_experiences": recalled,
            "strategy_choice": strategy_choice,
            "state": state,
            "regulation": regulation,
            "route": route,
            "pulse": pulse,
            "learning": learning,
            "experience_update": experience,
            "status": "self_managing_complete"
        }


self_managing_scs = SelfManagingSCS()