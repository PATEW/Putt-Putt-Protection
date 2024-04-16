import tkinter as tk
import random

SCOREBOARD_IMAGE = './resources/scoreboard.png'

class ScoreBoard:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=SCOREBOARD_IMAGE)
        self.scoreboard_label = tk.Label(self.window, image=self.image, borderwidth=0)
        self.scoreboard_label.pack()

        # Create a label for stroke count in the bottom right of the image
        self.bg_color = "#%02x%02x%02x" % (232, 185, 142)  # The brown background color
        self.text_color = "#%02x%02x%02x" % (65, 65, 65)  # The dark gray text color
        self.stroke_count_label = tk.Label(self.window, text="0", bg=self.bg_color, fg=self.text_color, font=("MS Sans Serif", 14))
        self.stroke_count_label.place(relx=0.95, rely=0.95, anchor='se')

        self.place_scoreboard()

    def place_scoreboard(self):
        screen_width = self.window.winfo_screenwidth()
        center_x = (screen_width - self.scoreboard_label.winfo_reqwidth()) // 2
        top_y = 0  # Top of the screen
        self.window.geometry(f'+{center_x}+{top_y}')

    def update_strokes(self, stroke_count):
        # Update the text of the stroke_count_label with the current stroke count
        self.stroke_count_label.config(text=f"{stroke_count}")


