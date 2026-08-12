from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from commands.handler import handle_command

app = FastAPI(title="Jarvis Backend")

# Allow dashboard access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Jarvis online"}

@app.post("/command")
async def command(data: dict):
    user = data.get("user")
    message = data.get("message")
    reply = await handle_command(user, message)
    return {"reply": reply}

@app.post("/voice")
async def voice(file: UploadFile):
    audio = await file.read()
    # Placeholder until speech-to-text is added
    return {"reply": "I heard your voice — speech-to-text coming soon."}
