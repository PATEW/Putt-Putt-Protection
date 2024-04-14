import tkinter as tk
import random

GOAL_IMAGE = './resources/goal.png'

class Goal:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=GOAL_IMAGE)  # Keep a reference to the image
        tk.Label(self.window, image=self.image, borderwidth=0).pack()
        self.placegoal()
    
    def placegoal(self):
        screen_width = self.window.winfo_screenwidth() # Screen dimensions
        screen_height = self.window.winfo_screenheight()
        goal_width = self.window.winfo_width() # Goal dimensions
        goal_height = self.window.winfo_height()
        x = random.randint(0, screen_width - goal_width)
        y = random.randint(0, screen_height - goal_height)
        self.window.geometry(f'+{x}+{y}')