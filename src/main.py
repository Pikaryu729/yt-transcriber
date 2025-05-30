import argparse
from dotenv import dotenv_values
from pathlib import Path
from download import download_youtube_audio
from summarize import summarize
from transcript import transcribe
from utils import read_text_file, save_to_file
import os

BASE_DIR = Path(__file__).resolve().parent.parent
AUDIO_DIR= BASE_DIR / "audios"
TRANSCRIPTION_DIR = BASE_DIR / "transcriptions"
SUMMARY_DIR = BASE_DIR / "summaries"
CONFIG = dotenv_values(BASE_DIR / ".env")


def main():
    parser = argparse.ArgumentParser(
        prog="transcript-yt",
        description="command line utility for downloading, transcribing, and summarizing youtube audio",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    download_parser = subparsers.add_parser("download", help="Download a video from a URL")
    download_parser.add_argument("url", help='The URL to download from')

    transcribe_parser = subparsers.add_parser("transcribe", help="Transcribe audio file")
    transcribe_parser.add_argument("audio", help='The filepath to transcribe from')

    summarize_parser= subparsers.add_parser("summarize", help="summarizes transcript file")
    summarize_parser.add_argument("transcript", help='The trancript to summarize')
    
    args = parser.parse_args() 

    if args.command == "download":
        download_youtube_audio(args.url, audio_dir=AUDIO_DIR)
    elif args.command == "transcribe":
        transcript = transcribe(audio_file=str(AUDIO_DIR / args.audio))
        output_file_name = os.path.splitext(args.audio)[0]
        save_to_file(text=transcript, file_path=str(TRANSCRIPTION_DIR / f"{output_file_name}.txt"))
    elif args.command == "summarize":
        transcription = read_text_file(str(TRANSCRIPTION_DIR / args.transcript))
        summary = summarize(transcription, config=CONFIG)
        save_to_file(summary, str(SUMMARY_DIR / args.transcript))


if __name__ == "__main__":
    main()