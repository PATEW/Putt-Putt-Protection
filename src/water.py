import tkinter as tk
import random
import re

WATER_IMAGE = './resources/water.png'

class Water:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=WATER_IMAGE)  # Keep a reference to the image
        self.water_label = tk.Label(self.window, image=self.image, borderwidth=0)
        self.water_label.pack()
        self.set_random_loc()

    def set_random_loc(self):
        screen_width = self.window.winfo_screenwidth()  # Screen dimensions
        screen_height = self.window.winfo_screenheight()
        water_width = self.window.winfo_width()  # water dimensions
        water_height = self.window.winfo_height()
        x = random.randint(0, screen_width - water_width)
        y = random.randint(0, screen_height - water_height)
        self.window.geometry(f'+{x}+{y}')

    def handle_collission(self, ball):
        water_pos = self.getLocation()
        water_dims = self.getDimensions()
        ball_pos = ball.getLocation()
        ball_dims = ball.getDimensions()
        ball_startPos = ball.getStartLocation()

    
        # Calculate water and ball boundaries
        water_left, water_top = water_pos
        water_right = water_left + water_dims[0]
        water_bottom = water_top + water_dims[1]
        ball_left, ball_top = ball_pos
        ball_right = ball_left + ball_dims[0]
        ball_bottom = ball_top + ball_dims[1]

        # Check for collision
        if (water_left <= ball_right and water_right >= ball_left and
            water_top <= ball_bottom and water_bottom >= ball_top):
            ball.window.geometry(f'+{ball_startPos[0]}+{ball_startPos[1]}')
            ball.stop_ball()
            return True
        return False

    def getLocation(self):
        return self.window.winfo_x(), self.window.winfo_y()

    def getDimensions(self):
        return self.water_label.winfo_width(), self.water_label.winfo_height()

    def getBounds(self):
        geometry = self.window.geometry()

        w, h, x, y = map(int, re.findall(r'(\d+)', geometry))
        return (x, y, x+w, y+h)