function updatePanel(index, text) {
    const panels = document.querySelectorAll(".status");

    if (panels[index]) {
        panels[index].textContent = text;
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function runSCS() {

    const question = document
        .getElementById("question")
        .value
        .trim();

    const answerPanel = document.getElementById("darrelAnswer");
    const startButton = document.getElementById("startPulse");

    if (!question) {
        alert("Please enter a question.");
        return;
    }

    startButton.disabled = true;
    startButton.textContent = "THINKING...";

    answerPanel.textContent = "DARREL is thinking...";

    updatePanel(0, "🧠 Searching memory...");
    updatePanel(1, "Waiting...");
    updatePanel(2, "Waiting...");
    updatePanel(3, "Waiting...");
    updatePanel(4, "Waiting...");
    updatePanel(5, "Waiting...");

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

        if (!response.ok) {
            throw new Error(
                "Server returned status " + response.status
            );
        }

        const result = await response.json();

        updatePanel(
            0,
            "🧠 " +
            (result.memory?.total_memories ?? 0) +
            " memories available"
        );

        await sleep(250);

        const leftResponse =
            result.left_brain?.llm_response ||
            result.left_brain?.analysis?.recommendation ||
            "Left Brain complete";

        updatePanel(
            1,
            "Confidence: " +
            Math.round(
                (result.left_brain?.confidence ?? 0) * 100
            ) +
            "%\n\n" +
            leftResponse
        );

        await sleep(250);

        const rightResponse =
            result.right_brain?.llm_response ||
            result.right_brain?.recommendation ||
            result.right_brain?.creative_summary?.recommendation ||
            "Right Brain complete";

        updatePanel(
            2,
            "Confidence: " +
            Math.round(
                (result.right_brain?.confidence ?? 0) * 100
            ) +
            "%\n\n" +
            rightResponse
        );

        await sleep(250);

        const synthesisResponse =
            result.synthesis?.combined_insight ||
            result.synthesis?.recommendation ||
            "Synthesis complete";

        updatePanel(
            3,
            synthesisResponse
        );

        await sleep(250);

        updatePanel(
            4,
            "Verdict: " +
            (result.verification?.verdict ?? "UNKNOWN") +
            "\nConfidence: " +
            Math.round(
                (result.verification?.confidence ?? 0) * 100
            ) +
            "%"
        );

        await sleep(250);

        const executiveDecision =
            result.executive?.executive_decision?.decision ||
            "No executive decision";

        updatePanel(
            5,
            executiveDecision
        );

        answerPanel.textContent =
            synthesisResponse ||
            leftResponse ||
            rightResponse ||
            "DARREL completed the cognitive pulse.";

    } catch (error) {

        answerPanel.textContent =
            "Error: " + error.message;

        document
            .querySelectorAll(".status")
            .forEach(panel => {
                panel.textContent = "Error";
            });

    } finally {

        startButton.disabled = false;
        startButton.textContent = "START PULSE";
    }
}