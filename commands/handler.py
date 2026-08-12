from commands.registry import COMMANDS, register
from modules.ai import ai_response
from modules.jarvis_voice import jarvis_voice

async def handle_command(user, message):
    parts = message.split(" ", 1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd in COMMANDS:
        return await COMMANDS[cmd](arg)

    return await ai_response(message)

@register("speak")
async def speak_command(arg):
    audio = await jarvis_voice(arg)
    return f"VOICE:{audio}"
