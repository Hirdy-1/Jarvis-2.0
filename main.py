from fastapi import FastAPI
import threading
from discord_bot import start_discord

app = FastAPI(title="Jarvis Backend")

@app.get("/")
def root():
    return {"status": "Jarvis online"}

# Start Discord bot in a separate thread
threading.Thread(target=start_discord).start()
