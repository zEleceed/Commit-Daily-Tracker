from pathlib import Path
from datetime import datetime


def append_comments(file_path: Path, comment:str):
    # Function to append a comment with current date/time to a students .txt
    current_date = datetime.now().strftime("%Y/%m/%d")
    with open(file_path, "a") as file:
        file.write(f"{current_date}: {comment}\n")
