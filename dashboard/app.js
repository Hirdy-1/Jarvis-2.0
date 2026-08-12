const BACKEND_URL = "https://jarvis-2-0-ej0m.onrender.com"; // change this

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
        const reply = data.reply;

        if (reply.startsWith("VOICE:")) {
            const base64Audio = reply.replace("VOICE:", "");
            playVoice(base64Audio);
            log("Jarvis (voice): Playing audio...");
        } else {
            log("Jarvis: " + reply);
        }

    } catch (err) {
        log("Error: Could not reach Jarvis backend.");
    }
}

function playVoice(base64Audio) {
    const audioElement = document.getElementById("jarvisAudio");
    const audioSrc = "data:audio/mp3;base64," + base64Audio;
    audioElement.src = audioSrc;
    audioElement.play();
}

let recorder;
let audioChunks = [];

async function startRecording() {
    log("Recording...");

    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);

    recorder.ondataavailable = e => audioChunks.push(e.data);

    recorder.onstop = async () => {
        const blob = new Blob(audioChunks, { type: "audio/wav" });
        audioChunks = [];

        const formData = new FormData();
        formData.append("file", blob);

        const response = await fetch(`${BACKEND_URL}/voice`, {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        log("Jarvis: " + data.reply);
    };

    recorder.start();
    setTimeout(() => recorder.stop(), 3000);
}
