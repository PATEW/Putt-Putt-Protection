import tkinter as tk
import pyautogui

CLUB_IMAGE = './resources/club.png'
COURSE_IMAGE = './resources/course.png'

# Club Window
club_window = tk.Tk()
club_window.overrideredirect(True)
club_window.wm_attributes("-transparentcolor", "white")

club_image = tk.PhotoImage(file=CLUB_IMAGE)
golf_club = tk.Label(club_window, image=club_image, borderwidth=0)
golf_club.pack()

# Course Window
course_window = tk.Toplevel()
course_window.overrideredirect(True)
course_window.wm_attributes("-transparentcolor", "white")

course_image = tk.PhotoImage(file=COURSE_IMAGE)
course = tk.Label(course_window, image=course_image, borderwidth=0)
course.pack(expand=True)

# Position the course window in the center
screen_width = course_window.winfo_screenwidth()
screen_height = course_window.winfo_screenheight()
center_x = int(screen_width / 2 - course.winfo_reqwidth() / 2)
center_y = int(screen_height / 2 - course.winfo_reqheight() / 2)
course_window.geometry(f'+{center_x}+{center_y}')

def periodic_update():
    x, y = pyautogui.position()
    club_window.geometry(f'+{x - golf_club.winfo_width() // 2}+{y - golf_club.winfo_height() // 2}')
    club_window.after(10, periodic_update)

if __name__ == '__main__':
    club_window.after(10, periodic_update)
    club_window.mainloop()
