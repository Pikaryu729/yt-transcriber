import yt_dlp 
import asyncio
from pathlib import Path

def download_youtube_audio(url, audio_dir: Path):
    """Downloads youtube video with the url in mp3 format and stores it in audios folder"""
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": str(audio_dir / "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
        }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return "Successfully downloaded audio file"
    except Exception as e:
        return f"Unexpected error {e}"