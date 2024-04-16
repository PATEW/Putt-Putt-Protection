import os
from pathlib import Path


NAMED_CONVERSION = "PUTT"

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
        try:
            for entry in os.scandir(dir):
                if entry.is_file():  # If it's file save and go next
                    yield entry
                else:  # If the entry is another directory, recall function
                    yield from scanDirRecursive(entry.path)
        except PermissionError:
            print("PermissionError Babyyy")
        except Exception:
            raise Exception

def check_collision(obj1, obj2):
    # Check for collision between two objects

    x1, y1, x2, y2 = obj1.getBounds()
    x3, y3, x4, y4 = obj2.getBounds()

    horizontal_collision = (x1 <= x4) and (x3 <= x2)
    vertical_colllision = (y1 <= y4) and (y3 <= y2)

    return horizontal_collision and vertical_colllision
