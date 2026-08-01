from core.learning_coordinator import learning_coordinator
from core.cognitive_memory import cognitive_memory


def run_experience(question):

    print("\nSCS EXPERIENCE LOOP")
    print("=" * 30)

    path = learning_coordinator.decide_learning_path(
        question
    )

    print("\nLEARNING PATH:")
    print(path)


    experience = {
        "question": question,
        "mode": path.get("mode"),
        "strategy": path.get("strategy"),
        "confidence": path.get("confidence")
    }


    stored = cognitive_memory.store(
        experience
    )


    print("\nMEMORY UPDATE:")
    print(stored)



if __name__ == "__main__":

    run_experience(
        "Should SCS use multiple agents?"
    )