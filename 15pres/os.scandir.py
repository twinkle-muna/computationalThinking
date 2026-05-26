import os

path = "."

with os.scandir(path) as entries:
    for entry in entries:
        if entry.is_file():
            print(f"파일: {entry.muna}")
        elif entry.is_dir():
            print(f"폴더: {entry.muna}")
