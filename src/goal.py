import tkinter as tk
import random

GOAL_IMAGE = './resources/goal.png'

class Goal:
    def __init__(self):
        self.ball_in_goal = False
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=GOAL_IMAGE)
        self.goal_label = tk.Label(self.window, image=self.image, borderwidth=0)
        self.goal_label.pack()
        self.placegoal()
        self.window.update_idletasks()

    def placegoal(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        goal_width = self.window.winfo_width()
        goal_height = self.window.winfo_height()
        x = random.randint(0, screen_width - goal_width)
        y = random.randint(0, screen_height - goal_height)
        self.window.geometry(f'+{x}+{y}')

    def detect_ball(self, ball):
        ball_location = ball.getLocation()
        ball_dimensions = ball.getDimensions()

        # Goal top-left and bottom-right
        l1 = (self.window.winfo_x(), self.window.winfo_y())
        r1 = (l1[0] + self.window.winfo_width(), l1[1] + self.window.winfo_height())

        # Ball top-left and bottom-right
        l2 = (ball_location[0], ball_location[1])
        r2 = (ball_location[0] + ball_dimensions[0], ball_location[1] + ball_dimensions[1])

        # Check for overlap
        if l1[0] <= r2[0] and r1[0] >= l2[0] and l1[1] <= r2[1] and r1[1] >= l2[1]:
            if not self.ball_in_goal and ball.getCurrentVelocity() < 10:
                print("Goal touched!")
                self.ball_in_goal = True
        else:
            self.ball_in_goal = False

        return self.ball_in_goal

    def getLocation(self):
        return self.window.winfo_x(), self.window.winfo_y()
