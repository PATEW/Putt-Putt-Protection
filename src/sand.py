import tkinter as tk
import random
import re

SAND_IMAGE = './resources/sand.png'

class Sand:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=SAND_IMAGE)  # Keep a reference to the image
        self.sand_label = tk.Label(self.window, image=self.image, borderwidth=0)
        self.sand_label.pack()
        self.place_sand()

    def place_sand(self):
        screen_width = self.window.winfo_screenwidth()  # Screen dimensions
        screen_height = self.window.winfo_screenheight()
        sand_width = self.window.winfo_width()  # sand dimensions
        sand_height = self.window.winfo_height()
        x = random.randint(0, screen_width - sand_width)
        y = random.randint(0, screen_height - sand_height)
        self.window.geometry(f'+{x}+{y}')

    def detect_collision_with_ball(self, ball):
        sand_pos = self.getLocation()
        sand_dims = self.getDimensions()
        ball_pos = ball.getLocation()
        ball_dims = ball.getDimensions()

        # Calculate sand and ball boundaries
        sand_left, sand_top = sand_pos
        sand_right = sand_left + sand_dims[0]
        sand_bottom = sand_top + sand_dims[1]
        ball_left, ball_top = ball_pos
        ball_right = ball_left + ball_dims[0]
        ball_bottom = ball_top + ball_dims[1]

        # Check for collision
        if (sand_left <= ball_right and sand_right >= ball_left and
            sand_top <= ball_bottom and sand_bottom >= ball_top):
            ball.deceleration_rate = 0.3
            return True
        ball.deceleration_rate = 0.1
        return False

    def getLocation(self):
        return self.window.winfo_x(), self.window.winfo_y()

    def getDimensions(self):
        return self.sand_label.winfo_width(), self.sand_label.winfo_height()

    def getBounds(self):
        geometry = self.window.geometry()

        x, y, w, h = map(int, re.findall(r'(\d+)', geometry))
        return (x, y, x+w, y+h)