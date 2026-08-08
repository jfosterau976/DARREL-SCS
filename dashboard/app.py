import os
import sys

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from flask import Flask, request, jsonify, render_template
from core.coordinator import coordinator


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    data = request.get_json()
    question = data.get("question", "")

    result = coordinator.process(question)

    execution = (
        result.get("pulse", {})
        .get("execution", {})
    )

    module_times = execution.get(
        "module_times_ms",
        {}
    )

    module_results = execution.get(
        "results",
        {}
    )

    print("\n=== DARREL MODULE TIMING ===")

    for module_name, milliseconds in module_times.items():

        print(
            f"{module_name}: "
            f"{milliseconds:.2f} ms "
            f"({milliseconds / 1000:.2f} sec)"
        )

    print("============================")

    print("\n=== OLLAMA LLM METRICS ===")

    metrics_found = False

    for module_name, module_result in module_results.items():

        if not isinstance(module_result, dict):
            continue

        output = module_result.get(
            "output",
            {}
        )

        if not isinstance(output, dict):
            continue

        llm_data = output.get(
            "llm",
            {}
        )

        if not isinstance(llm_data, dict):
            continue

        metrics = llm_data.get(
            "metrics"
        )

        if not isinstance(metrics, dict):
            continue

        metrics_found = True

        print(f"\n{module_name}:")

        print(
            "  prompt_eval_count:",
            metrics.get("prompt_eval_count")
        )

        print(
            "  eval_count:",
            metrics.get("eval_count")
        )

        prompt_duration = metrics.get(
            "prompt_eval_duration"
        )

        eval_duration = metrics.get(
            "eval_duration"
        )

        total_duration = metrics.get(
            "total_duration"
        )

        if prompt_duration is not None:
            print(
                "  prompt_eval:",
                f"{prompt_duration / 1_000_000_000:.2f} sec"
            )

        if eval_duration is not None:
            print(
                "  generation:",
                f"{eval_duration / 1_000_000_000:.2f} sec"
            )

        if total_duration is not None:
            print(
                "  ollama_total:",
                f"{total_duration / 1_000_000_000:.2f} sec"
            )

        if (
            metrics.get("eval_count")
            and eval_duration
        ):
            tokens_per_second = (
                metrics["eval_count"]
                / (
                    eval_duration
                    / 1_000_000_000
                )
            )

            print(
                "  generation_speed:",
                f"{tokens_per_second:.2f} tokens/sec"
            )

    if not metrics_found:
        print("No LLM metrics found.")

    print("==========================\n")

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )