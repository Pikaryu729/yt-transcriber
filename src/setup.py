from rich.prompt import Prompt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def main():
    api_key = Prompt.ask("Enter API Key", password=True)
    with open(str(BASE_DIR / ".env"), "w") as file:
        file.write(f"DEEPSEEK_API_KEY={api_key}")



if __name__ == "__main__":
    main()