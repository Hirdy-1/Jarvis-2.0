from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from commands.handler import handle_command

app = FastAPI(title="Jarvis Backend")

# CORS so dashboard can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow dashboard URL
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
