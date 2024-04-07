import os
from pathlib import Path


EXCLUDE_DIRS = [
    "./.venv",
    "./venv",
    "~",
    str(Path.home()),
    "./.git",
    "./__pycache__",
    "..",
]


def scanDirRecursive(dir: str = "target_dir"):
    if dir not in EXCLUDE_DIRS:
        for entry in os.scandir(dir):
            if entry.is_file():  # If it's file save and go next
                yield entry
            else:  # If the entry is another directory, recall function
                yield from scanDirRecursive(entry.path)
