from elevenlabs import ElevenLabs
import base64
import os

# Load API key from Render environment variables
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Jarvis-style British male voice (free tier compatible)
VOICE_ID = "pNInz6obpgDQGcFmaJgB"

async def jarvis_voice(text):
    # Generate audio using ElevenLabs neural TTS
    audio = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        model_id="eleven_multilingual_v2",
        text=text
    )

    # Save MP3 file
    with open("jarvis_voice.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)

    # Convert MP3 → base64 for dashboard playback
    with open("jarvis_voice.mp3", "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
