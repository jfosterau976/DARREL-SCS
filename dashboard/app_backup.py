import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from flask import Flask, render_template_string, request

from core.orchestrated_scs_v2 import orchestrated_scs_v2

from core.orchestrated_scs_v2 import orchestrated_scs_v2


app = Flask(__name__)


HTML = """
<!DOCTYPE html>
<html>
<head>
<title>SCS Dashboard</title>

<style>

body {
    font-family: Arial, sans-serif;
    background:#111;
    color:#eee;
    padding:30px;
}

.card {
    background:#1d1d1d;
    padding:20px;
    margin:15px 0;
    border-radius:10px;
}

h1 {
    color:#00ffcc;
}

.left {
    color:#4da6ff;
}

.right {
    color:#cc66ff;
}

.learn {
    color:#66ff66;
}

.decision {
    color:#ffcc00;
}

pre {
    white-space:pre-wrap;
}

</style>

</head>


<body>

<h1>⚡ Synthetic Cognitive System</h1>


<div class="card">

<form method="post">

<input 
name="question"
style="width:70%;padding:10px"
placeholder="Ask SCS..."
>

<button 
style="padding:10px"
>
Run Pulse
</button>

</form>

</div>



{% if 
 %}


<div class="card">

<h2>⚡ Selective Pulse</h2>

<p>Status:
{{result.status}}
</p>

</div>



<div class="card left">

<h2>🔵 Left Reasoning</h2>

<pre>
{{result.left_reasoning}}
</pre>

</div>



<div class="card right">

<h2>🟣 Right Reasoning</h2>

<pre>
{{result.right_reasoning}}
</pre>

</div>



<div class="card">

<h2>🟢 Synthesis</h2>

<pre>
{{result.synthesis}}
</pre>

</div>



<div class="card">

<h2>🟡 Verification</h2>

<pre>
{{result.verification}}
</pre>

</div>



<div class="card decision">

<h2>🎯 Executive Decision</h2>

<pre>
{{result.base_result.decision}}
</pre>

</div>



<div class="card learn">

<h2>🧬 Learning</h2>

<pre>
{{result.base_result.learning}}
</pre>

</div>


{% endif %}


</body>
</html>
"""


@app.route("/", methods=["GET","POST"])
def home():

    result = None


    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if not question:
            question = "How can SCS improve its own reasoning process?"


        result = orchestrated_scs_v2.think(
            question
        )


        class Wrapper:

            def __init__(self,data):

                self.__dict__.update(data)


        result = Wrapper(result)


    return render_template_string(
        HTML,
        result=result
    )



if __name__ == "__main__":

    app.run(
        debug=True
    )