import tkinter as tk
import pyautogui
import ball

CLUB_IMAGE = './resources/club.png'
COURSE_IMAGE = './resources/course.png'

# Function to reassert window stacking order
def reassert_order():
    course_window.lift()
    ball_instance.ball_window.lift()
    club_window.lift()

# Club Window
club_window = tk.Tk()
club_window.overrideredirect(True)
club_window.wm_attributes("-transparentcolor", "white")
club_window.wm_attributes("-topmost", True)

club_image = tk.PhotoImage(file=CLUB_IMAGE)
club = tk.Label(club_window, image=club_image, borderwidth=0)
club.pack()

# Course Window
course_window = tk.Toplevel()
course_window.overrideredirect(True)
course_window.wm_attributes("-transparentcolor", "white")
course_window.wm_attributes("-topmost", True)

course_image = tk.PhotoImage(file=COURSE_IMAGE)
course = tk.Label(course_window, image=course_image, borderwidth=0)
course.pack(expand=True)

# Position the course window in the center
screen_width = course_window.winfo_screenwidth()
screen_height = course_window.winfo_screenheight()
center_x = int(screen_width / 2 - course.winfo_reqwidth() / 2)
center_y = int(screen_height / 2 - course.winfo_reqheight() / 2)
course_window.geometry(f'+{center_x}+{center_y}')

# Make ball
x, y = pyautogui.position()
ball_instance = ball.Ball()

# Bind the focus in event to reassert order
club_window.bind("<FocusIn>", lambda e: reassert_order())
course_window.bind("<FocusIn>", lambda e: reassert_order())

# Initial stacking order
reassert_order()

def periodic_update():
    x, y = pyautogui.position()
    club_window.geometry(f'+{x - club.winfo_width() // 2}+{y - club.winfo_height() // 2}')
    club_window.after(10, periodic_update)

if __name__ == '__main__':
    club_window.after(10, periodic_update)
    club_window.mainloop()
