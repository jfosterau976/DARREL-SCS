import sys
import os
import json
from datetime import datetime

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)

from core.orchestrated_scs_v2 import orchestrated_scs_v2


QUESTIONS_FILE = "benchmarks/tests/questions.json"
RESULTS_FILE = "benchmarks/results/results.json"


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

    print("🧠 DARREL Benchmark Starting")

    questions = load_questions()

    results = {
        "timestamp": str(datetime.now()),
        "system": "DARREL SCS",
        "results": []
    }

    for item in questions:

        print("\nTesting:")
        print(item["question"])

        response = orchestrated_scs_v2.think(
            item["question"]
        )

        results["results"].append(
            {
                "id": item["id"],
                "category": item["category"],
                "question": item["question"],
                "response": response
            }
        )

    save_results(results)

    print("\n✅ Benchmark Complete")
    print("Saved:", RESULTS_FILE)


if __name__ == "__main__":
    run()