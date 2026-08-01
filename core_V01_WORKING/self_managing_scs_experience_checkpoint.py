from core.cognitive_state_manager import cognitive_state
from core.cognitive_regulation_engine import cognitive_regulation
from core.pulse_intelligence_router import pulse_router
from core.selective_pulse_engine import selective_pulse_engine
from core.adaptive_learning_loop import adaptive_learning_loop
from core.experience_replay_engine import experience_replay


class SelfManagingSCS:

    def __init__(self):
        self.name = "SCS Self Managing Cognitive System"


    def think(self, question):

        recalled = experience_replay.recall(question)

        state = cognitive_state.evaluate(
            question,
            0.5
        )

        regulation = cognitive_regulation.regulate(
            state
        )

        route = pulse_router.route(
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

        experience = experience_replay.store({
            "question": question,
            "strategy": route["activated_modules"],
            "status": "completed"
        })

        return {
            "system": self.name,
            "recalled_experiences": recalled,
            "state": state,
            "regulation": regulation,
            "route": route,
            "pulse": pulse,
            "learning": learning,
            "experience_update": experience,
            "status": "self_managing_complete"
        }


self_managing_scs = SelfManagingSCS()