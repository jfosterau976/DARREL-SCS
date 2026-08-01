from core.cognitive_state_manager import cognitive_state
from core.cognitive_regulation_engine import cognitive_regulation
from core.pulse_intelligence_router import pulse_router
from core.selective_pulse_engine import selective_pulse_engine
from core.adaptive_learning_loop import adaptive_learning_loop
from core.experience_replay_engine import experience_replay
from core.experience_strategy_selector import experience_strategy_selector
from core.goal_planning_engine import goal_planner
from core.goal_feedback_engine import goal_feedback


class SelfManagingSCS:

    def __init__(self):
        self.name = "SCS Self Managing Cognitive System"


    def think(self, question):

        goal = goal_planner.create_goal(
            question
        )

        plan = goal_planner.create_plan(
            goal
        )

        recalled = experience_replay.recall(
            question
        )

        strategy_choice = experience_strategy_selector.select(
            recalled["matches"]
        )

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

        feedback = goal_feedback.evaluate(
            goal,
            plan,
            pulse
        )

        experience = experience_replay.store({
            "question": question,
            "strategy": strategy_choice["strategy"],
            "goal": goal["goal"],
            "feedback": feedback["success"],
            "status": "completed"
        })

        return {
            "system": self.name,
            "goal": goal,
            "plan": plan,
            "strategy_choice": strategy_choice,
            "state": state,
            "regulation": regulation,
            "route": route,
            "pulse": pulse,
            "learning": learning,
            "feedback": feedback,
            "experience_update": experience,
            "status": "self_managing_complete"
        }


self_managing_scs = SelfManagingSCS()