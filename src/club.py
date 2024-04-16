import math
import tkinter as tk
from PIL import Image, ImageTk
import re

CLUB_IMAGE = './resources/club.png'
CLUB_SIZE = (200, 350) #Width and Height for the Club Label (No math behind it, just tested)

class Club:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "black", "-topmost", True)
        self.image = ImageTk.PhotoImage(file=CLUB_IMAGE)
        self.label = tk.Label(self.window, image=self.image, borderwidth=0, width=CLUB_SIZE[0], height=CLUB_SIZE[1])
        self.label.pack()

    def rotate_club(self, x, y, ball):
        ball_location = ball.getLocation()
        current_state = ball.current_state
        
        if current_state == "idle":    
            # Rotate the image based on the given angle
            if y - ball_location[1] == 0 or x - ball_location[0] == 0:
                return    
            angle =  abs(math.atan((y - ball_location[1])/(x - ball_location[0])) * 180 / math.pi)
            first_Image = Image.open(CLUB_IMAGE)
            rotated_image = first_Image.rotate(angle, expand=True)
            rotated_tk_image = ImageTk.PhotoImage(rotated_image)
            label = self.label
            label.config(image=rotated_tk_image)
            label.image = rotated_tk_image  # prevent garbage collection
            self.window.geometry(f'+{x - self.window.winfo_width() // 2}+{y - self.window.winfo_height() // 2}')

        elif current_state == "drag":
            if y - ball_location[1] == 0 or x - ball_location[0] == 0:
                return    
            angle =  ((y - ball_location[1]) + (x - ball_location[0])/2) * 2 / math.pi
            first_Image = Image.open(CLUB_IMAGE)
            rotated_image = first_Image.rotate(angle, expand=True)
            rotated_tk_image = ImageTk.PhotoImage(rotated_image)
            label = self.label
            label.config(image=rotated_tk_image)
            label.image = rotated_tk_image
        
        else:
            self.window.geometry(f'+{x - self.window.winfo_width() // 2}+{y - self.window.winfo_height() // 2}')
        
       
    def getBounds(self):
        geometry = self.window.geometry()

        x, y, w, h = map(int, re.findall(r'(\d+)', geometry))
        return (x, y, x+w, y+h)