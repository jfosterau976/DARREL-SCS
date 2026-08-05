from agents.memory_agent import memory_agent
from agents.learning_agent import learning_agent
from agents.optimizer_agent import optimizer_agent
from core.improvement_memory import improvement_memory


class ReflectionLoop:

    def __init__(self):
        self.name = "SCS Reflection Loop"


    def reflect(self):

        print("\n🔄 REFLECTION LOOP START")


        memory = memory_agent.load_memory()

        history = memory.get("memories", [])


        print("\nMemories analysed:")
        print(len(history))


        lessons = learning_agent.learn(history)


        print("\nLessons:")
        print(lessons)


        optimisation = optimizer_agent.optimize(
            lessons.get("lessons", [])
        )


        print("\nOptimisation:")
        print(optimisation)


        recommendations = optimisation.get(
            "recommendations",
            []
        )


        saved = []

        for recommendation in recommendations:

            result = improvement_memory.save_improvement(
                recommendation
            )

            saved.append(result)


        print("\nImprovement Memory:")
        print(saved)


        return {
            "lessons": lessons,
            "optimisation": optimisation,
            "improvements_saved": saved
        }


reflection_loop = ReflectionLoop()