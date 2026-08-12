import os
import asyncio
import discord
import httpx

TOKEN = os.getenv("DISCORD_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def send_to_backend(user, message):
    async with httpx.AsyncClient() as req:
        r = await req.post(f"{BACKEND_URL}/command", json={
            "user": user,
            "message": message
        })
        return r.json().get("reply", "Jarvis had no response")

@client.event
async def on_ready():
    print(f"Jarvis connected as {client.user}")

@client.event
async def on_message(msg):
    if msg.author.bot:
        return

    user = str(msg.author)
    message = msg.content

    reply = await send_to_backend(user, message)
    await msg.channel.send(reply)

def start_discord():
    client.run(TOKEN)
