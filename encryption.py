import os


def scanDirRecursive(dir: str):
    for entry in os.scandir(dir):
        if entry.is_file():  # If it's file save and go next
            yield entry.path  # We want to know where did the file came from
        else:  # If the entry is another directory, recall function
            yield from scanDirRecursive(entry.path)


for items in scanDirRecursive("target_dir"):
    print(items)
