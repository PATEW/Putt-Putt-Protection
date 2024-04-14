import tkinter as tk
import random

GOAL_IMAGE = "./resources/goal.png"


class Goal:
    def __init__(self):
        self.ball_in_goal = False
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=GOAL_IMAGE)  # Keep a reference to the image
        tk.Label(self.window, image=self.image, borderwidth=0).pack()
        self.placegoal()

    def placegoal(self):
        screen_width = self.window.winfo_screenwidth()  # Screen dimensions
        screen_height = self.window.winfo_screenheight()
        goal_width = self.window.winfo_width()  # Goal dimensions
        goal_height = self.window.winfo_height()
        x = random.randint(0, screen_width - goal_width)
        y = random.randint(0, screen_height - goal_height)
        self.window.geometry(f"+{x}+{y}")

    def detect_ball(self, ball):
        ball_location = ball.getLocation()
        ball_dimensions = ball.getDimensions()

        # Goal top-left and bottom-right
        l1 = (self.window.winfo_x(), self.window.winfo_y())
        r1 = (l1[0] + self.window.winfo_width(), l1[1] + self.window.winfo_height())

        # Ball top-left and bottom-right
        l2 = (ball_location[0], ball_location[1])
        r2 = (
            ball_location[0] + ball_dimensions[0],
            ball_location[1] + ball_dimensions[1],
        )

        # Check if one rectangle is on the left side of the other
        if l1[0] > r2[0] or l2[0] > r1[0]:
            isDetected = False
        # Check if one rectangle is above the other
        elif l1[1] > r2[1] or l2[1] > r1[1]:
            isDetected = False
        else:
            isDetected = True

        # Check the current detection state against the flag
        if isDetected:
            if not self.ball_in_goal:  # Ball has just entered the goal
                print("Goal touched!")
                self.ball_in_goal = True
        else:
            self.ball_in_goal = False  # Ball is not in the goal, reset flag

        return isDetected
