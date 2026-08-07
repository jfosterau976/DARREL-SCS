function updatePanel(index, text) {
    const panels = document.querySelectorAll(".status");
    panels[index].textContent = text;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function runSCS() {

    const question = document.getElementById("question").value.trim();

    if (!question) {
        alert("Please enter a question.");
        return;
    }

    updatePanel(0,"🧠 Searching memory...");
    updatePanel(1,"Waiting...");
    updatePanel(2,"Waiting...");
    updatePanel(3,"Waiting...");
    updatePanel(4,"Waiting...");
    updatePanel(5,"Waiting...");

    await sleep(250);

    const response = await fetch("/process",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            question:question
        })
    });

    const result = await response.json();

    updatePanel(
        0,
        "🧠 " +
        (result.memory?.total_memories ?? 0) +
        " memories available"
    );

    await sleep(250);

    updatePanel(
        1,
        "✅ Complete (" +
        Math.round((result.left_brain?.confidence ?? 0)*100) +
        "%)"
    );

    await sleep(250);

    updatePanel(
        2,
        "✅ Complete (" +
        Math.round((result.right_brain?.confidence ?? 0)*100) +
        "%)"
    );

    await sleep(250);

    updatePanel(
        3,
        "🟨 Synthesis Complete"
    );

    await sleep(250);

    updatePanel(
        4,
        "🟩 " +
        result.verification.verdict +
        " (" +
        Math.round(result.verification.confidence*100) +
        "%)"
    );

    await sleep(250);

    updatePanel(
        5,
        "⭐ " +
        (result.executive?.executive_decision?.decision ?? "ACCEPT")
    );
}