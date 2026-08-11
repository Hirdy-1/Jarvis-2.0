from fastapi import FastAPI
from commands.handler import handle_command

app = FastAPI(title="Jarvis Backend")

@app.get("/")
def root():
    return {"status": "Jarvis online"}

@app.post("/command")
async def command(data: dict):
    user = data.get("user")
    message = data.get("message")

    response = await handle_command(user, message)
    return {"reply": response}
