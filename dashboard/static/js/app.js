function updatePanel(id, title, content) {
    const panel = document.getElementById(id);

    if (!panel) return;

    let summary = "No data";

    if (!content || Object.keys(content).length === 0) {
        summary = "No data";
    }
    else if (id === "leftPanel") {
        summary =
            content.analysis?.recommendation ||
            content.llm_response ||
            "Left Brain complete";
    }
    else if (id === "rightPanel") {
        summary =
            content.llm_response ||
            "Right Brain complete";
    }
    else if (id === "synthesisPanel") {
        summary =
            content.combined_insight ||
            content.recommendation ||
            content.llm_response ||
            "Synthesis complete";
    }
    else if (id === "verificationPanel") {
        summary =
            "Verdict: " +
            (content.verdict || "UNKNOWN") +
            "\nConfidence: " +
            Math.round((content.confidence || 0) * 100) +
            "%";
    }
    else if (id === "memoryPanel") {
        summary =
            content.status ||
            "Memory inactive";
    }
    else if (id === "executivePanel") {
        summary =
            content.status ||
            "Executive inactive";
    }
    else if (content.llm_response) {
        summary = content.llm_response;
    }
    else if (content.combined_insight) {
        summary = content.combined_insight;
    }
    else if (content.verdict) {
        summary =
            "Verdict: " +
            content.verdict +
            "\nConfidence: " +
            Math.round((content.confidence || 0) * 100) +
            "%";
    }
    else if (content.status) {
        summary = content.status;
    }
    else {
        summary = "Module complete";
    }

    panel.textContent =
        title +
        "\n\n" +
        String(summary).substring(0, 600);
}


function loadPresetQuestion() {
    const value =
        document.getElementById("questionPreset").value;

    document.getElementById("question").value = value;
}


async function runSCS() {
    const question =
        document.getElementById("question").value.trim();

    const answer =
        document.getElementById("darrelAnswer");

    const button =
        document.getElementById("startPulse");

    if (!question) {
        alert("Please enter a question");
        return;
    }

    button.disabled = true;
    button.textContent = "THINKING...";

    try {
        const response = await fetch("/process", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const result = await response.json();

        const execution =
            result.pulse?.execution?.results || {};

        const leftBrain =
            execution.left_reasoning?.output ||
            result.left_brain ||
            {};

        const rightBrain =
            execution.right_reasoning?.output ||
            result.right_brain ||
            {};

        const synthesis =
            execution.synthesis?.output ||
            result.synthesis ||
            {};

        const verifier =
            execution.verifier?.output ||
            result.verification ||
            {};

        const executive =
            result.executive || {};

        updatePanel(
            "memoryPanel",
            "Memory",
            result.memory
        );

        updatePanel(
            "leftPanel",
            "Left Brain",
            leftBrain
        );

        updatePanel(
            "rightPanel",
            "Right Brain",
            rightBrain
        );

        updatePanel(
            "synthesisPanel",
            "Synthesis",
            synthesis
        );

        updatePanel(
            "verificationPanel",
            "Verifier",
            verifier
        );

        updatePanel(
            "executivePanel",
            "Executive",
            executive
        );

        answer.textContent =
            synthesis.combined_insight ||
            leftBrain.llm_response ||
            "DARREL completed pulse.";
    }
    catch (error) {
        answer.textContent =
            "ERROR: " + error.message;
    }
    finally {
        button.disabled = false;
        button.textContent = "START PULSE";
    }
}