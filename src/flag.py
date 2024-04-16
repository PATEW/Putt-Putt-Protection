import tkinter as tk
import random
import re

FLAG_IMAGE = './resources/flag.png'

class Flag:
    def __init__(self, goal):
        self.window = tk.Toplevel(goal.window)  # Set the flag window as a child of the goal window
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=FLAG_IMAGE)
        self.flag_label = tk.Label(self.window, image=self.image, borderwidth=0)
        self.flag_label.pack()
        self.place_flag(goal)

    def place_flag(self, goal):
        # Use the goal's window info directly
        x = goal.window.winfo_x()
        y = goal.window.winfo_y()
        goal_width = goal.window.winfo_width()
        goal_height = goal.window.winfo_height()
        # Adjust flag position to be on top of the goal, center it if needed
        self.window.geometry(f"+{x + goal_width // 2 - self.image.width() // 2}+{y + goal_height // 2 - self.image.height() // 2}")
    

    def getBounds(self):
        geometry = self.window.geometry()

        w, h, x, y = map(int, re.findall(r'(\d+)', geometry))
        return (x, y, x+w, y+h)
