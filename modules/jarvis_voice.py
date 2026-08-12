import azure.cognitiveservices.speech as speechsdk
import base64
import os

async def jarvis_voice(text):
    speech_key = os.getenv("AZURE_SPEECH_KEY")
    speech_region = os.getenv("AZURE_SPEECH_REGION")

    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key,
        region=speech_region
    )

    # Jarvis-style voice (British, calm, neural)
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"

    audio_config = speechsdk.audio.AudioOutputConfig(filename="jarvis_voice.mp3")
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    synthesizer.speak_text_async(text).get()

    with open("jarvis_voice.mp3", "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
