import tkinter as tk

CLUB_IMAGE = './resources/club.png'

class Club:
    def __init__(self):
        self.window = tk.Tk()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.club_image = tk.PhotoImage(file=CLUB_IMAGE)  # Keep a reference to the image
        tk.Label(self.window, image=self.club_image, borderwidth=0).pack()
