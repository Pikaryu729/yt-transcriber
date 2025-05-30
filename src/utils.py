from pathlib import Path


def read_text_file(file_path: Path):
    with open(file_path, "r") as file:
        contents = file.read()
    return contents


def save_to_file(text: str, file_path: Path):
    with open(file_path, "w") as file:
        file.write(text)
