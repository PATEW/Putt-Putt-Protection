import tkinter as tk
import pyautogui
from PIL import Image, ImageTk

CLUB_IMAGE = './resources/club.png'
COURSE_IMAGE = './resources/course.png'

def update_position():
    x, y = pyautogui.position()
    overlay_window.geometry(f'+{x - offset_x}+{y - offset_y}')

def periodic_update():
    update_position()
    overlay_window.after(10, periodic_update)

def show_course(window, course_image):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - course_image.width()) // 2
    y = (screen_height - course_image.height()) // 2
    golf_course = tk.Label(window, image=course_image, bd=0)
    golf_course.place(x=x, y=y)

if __name__ == '__main__':
    # Main window for the course
    window = tk.Tk()
    window.overrideredirect(True)
    window.attributes('-topmost', True)
    window.geometry(f'{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0')
    window.attributes('-alpha', 0.0)  # Make the window fully transparent

    # Load course image
    course_photo = ImageTk.PhotoImage(file=COURSE_IMAGE)
    show_course(window, course_photo)

    # Overlay window for the club
    overlay_window = tk.Toplevel(window)
    overlay_window.overrideredirect(True)
    overlay_window.attributes('-topmost', True)
    
    # Load club image
    club_image = Image.open(CLUB_IMAGE)
    club_photo = ImageTk.PhotoImage(club_image)
    golf_club = tk.Label(overlay_window, image=club_photo, bg='white')
    golf_club.pack()

    # Offset to center the club on the cursor
    offset_x = club_image.width // 2
    offset_y = club_image.height // 2

    # Update club position
    periodic_update()

    # Start main loop
    window.mainloop()

