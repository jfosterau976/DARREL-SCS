import json
from datetime import datetime


QUESTIONS_FILE = "benchmarks/tests/questions.json"
RESULTS_FILE = "benchmarks/results/baseline_results.json"


def load_questions():

    with open(QUESTIONS_FILE, "r") as f:
        return json.load(f)


def save_results(results):

    with open(RESULTS_FILE, "w") as f:
        json.dump(
            results,
            f,
            indent=4
        )


def run():

    print("🧠 Baseline Test Starting")

    questions = load_questions()

    results = {
        "timestamp": str(datetime.now()),
        "system": "Single Agent Baseline",
        "results": []
    }


    for item in questions:

        print("\nTesting:")
        print(item["question"])

        response = {
            "response": "Single agent response simulation for: "
                        + item["question"],
            "confidence": 0.5
        }


        results["results"].append(
            {
                "id": item["id"],
                "category": item["category"],
                "question": item["question"],
                "response": response
            }
        )


    save_results(results)

    print("\n✅ Baseline Complete")
    print("Saved:", RESULTS_FILE)


if __name__ == "__main__":
    run()