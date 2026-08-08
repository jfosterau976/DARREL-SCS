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

    question = data.get(
        "question",
        ""
    )

    result = coordinator.process(
        question
    )

    print(result)
    return jsonify(result)


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )