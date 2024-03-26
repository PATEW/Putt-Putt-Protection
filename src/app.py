import tkinter as tk
import pyautogui

CLUB_IMAGE = './resources/club.png'
window = tk.Tk()  # Create window
club_image = tk.PhotoImage(file=CLUB_IMAGE)
golf_club = tk.Label(window, image=club_image)  # Label for the image

def periodic_update():
    update_image_position()
    window.after(10, periodic_update)  # Schedule next update

def update_image_position():
    x, y = pyautogui.position()
    window.geometry(f'+{x - golf_club.winfo_width() // 2}+{y - golf_club.winfo_height() // 2}')

if __name__ == '__main__':
    window.overrideredirect(True)  # Hide the window border
    golf_club.pack()
    window.after(10, periodic_update)
    window.mainloop()

