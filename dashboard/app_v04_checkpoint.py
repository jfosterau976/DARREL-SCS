import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, render_template
from core.orchestrated_scs_v2 import orchestrated_scs_v2

app = Flask(__name__)


@app.route("/")
def home():
    result = orchestrated_scs_v2.think(
        "Should SCS use multiple agents?"
    )

    return render_template(
        "index.html",
        data=result
    )


@app.route("/think")
def think():
    result = orchestrated_scs_v2.think(
        "Should SCS use multiple agents?"
    )

    return jsonify(result)


@app.route("/status")
def status():
    return jsonify({
        "system": "SCS Dashboard",
        "status": "online",
        "version": "0.1"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )