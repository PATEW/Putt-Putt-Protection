import tkinter as tk
import random
import re

TREE_IMAGE = './resources/tree.png'

class Tree:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=TREE_IMAGE)  # Keep a reference to the image
        self.tree_label = tk.Label(self.window, image=self.image, borderwidth=0)
        self.tree_label.pack()
        self.set_random_loc()

    def set_random_loc(self):
        screen_width = self.window.winfo_screenwidth()  # Screen dimensions
        screen_height = self.window.winfo_screenheight()
        tree_width = self.window.winfo_width()  # Tree dimensions
        tree_height = self.window.winfo_height()
        x = random.randint(0, screen_width - tree_width)
        y = random.randint(0, screen_height - tree_height)
        self.window.geometry(f'+{x}+{y}')

    def handle_collission(self, ball):
        tree_pos = self.getLocation()
        tree_dims = self.getDimensions()
        ball_pos = ball.getLocation()
        ball_dims = ball.getDimensions()

        # Calculate tree and ball boundaries
        tree_left, tree_top = tree_pos
        tree_right = tree_left + tree_dims[0]
        tree_bottom = tree_top + tree_dims[1]
        ball_left, ball_top = ball_pos
        ball_right = ball_left + ball_dims[0]
        ball_bottom = ball_top + ball_dims[1]

        # Check for collision
        if (tree_left <= ball_right and tree_right >= ball_left and
            tree_top <= ball_bottom and tree_bottom >= ball_top):
            # Determine the side of the collision
            overlap_left = ball_right - tree_left
            overlap_right = tree_right - ball_left
            overlap_top = ball_bottom - tree_top
            overlap_bottom = tree_bottom - ball_top

            # Resolve collision by finding the minimum overlap
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
            if min_overlap == overlap_left:
                ball.velocity_x = -abs(ball.velocity_x)  # Reflect left
            elif min_overlap == overlap_right:
                ball.velocity_x = abs(ball.velocity_x)  # Reflect right
            elif min_overlap == overlap_top:
                ball.velocity_y = -abs(ball.velocity_y)  # Reflect up
            elif min_overlap == overlap_bottom:
                ball.velocity_y = abs(ball.velocity_y)  # Reflect down

            return True
        return False

    def getLocation(self):
        return self.window.winfo_x(), self.window.winfo_y()
    
    def getBounds(self):
        geometry = self.window.geometry()

        w, h, x, y = map(int, re.findall(r'(\d+)', geometry))
        return (x, y, x+w, y+h)

    def getDimensions(self):
        return self.tree_label.winfo_width(), self.tree_label.winfo_height()
