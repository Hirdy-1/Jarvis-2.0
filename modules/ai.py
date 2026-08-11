import os
import httpx

API_KEY = os.getenv("AI_KEY")

async def ai_response(message):
    return f"Jarvis thinking… You said: {message}"
