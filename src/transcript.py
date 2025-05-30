from pathlib import Path
import whisper


def transcribe(audio_file: str, model_name: str = "base"):
    """Takes in a file name from the audios directory and returns the transcribed text"""
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_file)
    return result["text"]
