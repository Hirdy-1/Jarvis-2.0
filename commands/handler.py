from commands.registry import COMMANDS
from modules.ai import ai_response
from modules.system import system_info

async def handle_command(user, message):
    parts = message.split(" ", 1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd in COMMANDS:
        return await COMMANDS[cmd](arg)

    # fallback to AI
    return await ai_response(message)
