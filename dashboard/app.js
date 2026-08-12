const BACKEND_URL = "https://jarvis-backend.onrender.com"; // change this

function log(text) {
    const consoleBox = document.getElementById("console");
    consoleBox.innerHTML += `<div>> ${text}</div>`;
    consoleBox.scrollTop = consoleBox.scrollHeight;
}

async function sendCommand() {
    const input = document.getElementById("commandInput");
    const message = input.value.trim();
    if (!message) return;

    log("You: " + message);
    input.value = "";

    try {
        const response = await fetch(`${BACKEND_URL}/command`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                user: "Dashboard",
                message: message
            })
        });

        const data = await response.json();
        log("Jarvis: " + data.reply);

    } catch (err) {
        log("Error: Could not reach Jarvis backend.");
    }
}
