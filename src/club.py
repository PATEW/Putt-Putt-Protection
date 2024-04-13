import math
import tkinter as tk
from PIL import Image, ImageTk

CLUB_IMAGE = './resources/club.png'
OLD_BALL_LOCATION = (0, 0)

class Club:
    def __init__(self):
        self.window = tk.Tk()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = ImageTk.PhotoImage(file=CLUB_IMAGE)
        self.label = tk.Label(self.window, image=self.image, borderwidth=0)
        self.label.pack()
        self.old_ball_location = OLD_BALL_LOCATION

    def rotate_club(self, x, y, ball_location):
        if ball_location != self.old_ball_location:
            self.old_ball_location= ball_location
            return
        # Rotate the image based on the given angle
        if y - ball_location[1] == 0 or x - ball_location[0] == 0:
            return    
        angle =  math.atan((y - ball_location[1])/(x - ball_location[0])) * 180 / math.pi
        first_Image = Image.open(CLUB_IMAGE)
        rotated_image = first_Image.rotate(angle, expand=True)
        rotated_tk_image = ImageTk.PhotoImage(rotated_image)
        label = self.label
        label.config(image=rotated_tk_image)
        label.image = rotated_tk_image  # prevent garbage collection
        self.old_ball_location = ball_location
        
    
       
