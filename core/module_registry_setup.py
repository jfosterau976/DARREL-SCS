from core.module_registry import module_registry

from core.goal_planning_engine import goal_planner
from core.left_brain import left_brain
from core.right_brain import right_brain
from core.synthesis_agent import synthesis_agent
from core.verifier_engine import verifier_engine
from core.reflection_agent import reflection_agent
from core.learning_extractor import learning_extractor


def register_modules():

    module_registry.register(
        "goal_planning",
        goal_planner
    )

    module_registry.register(
        "left_reasoning",
        left_brain
    )

    module_registry.register(
        "right_reasoning",
        right_brain
    )

    module_registry.register(
        "synthesis",
        synthesis_agent
    )

    module_registry.register(
        "verifier",
        verifier_engine
    )

    module_registry.register(
        "reflection",
        reflection_agent
    )

    module_registry.register(
        "learning",
        learning_extractor
    )


register_modules()


def get_registry():

    return module_registry