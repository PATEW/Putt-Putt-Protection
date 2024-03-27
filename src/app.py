import pyautogui
import course, ball, club

# Function to reassert window stacking order
def reassert_order():
    course.window.lift()
    ball.window.lift()
    club.window.lift()

def periodic_update():
    x, y = pyautogui.position()
    club_window_width = club.window.winfo_width()
    club_window_height = club.window.winfo_height()
    club.window.geometry(f'+{x - club_window_width // 2}+{y - club_window_height // 2}')
    club.window.after(10, periodic_update)

if __name__ == '__main__':
    club = club.Club()
    course = course.Course()
    ball = ball.Ball()

    club.window.bind("<FocusIn>", lambda e: reassert_order())    # Bind the focus in event to reassert order
    course.window.bind("<FocusIn>", lambda e: reassert_order())

    reassert_order() # Initial stacking order

    club.window.after(10, periodic_update)
    club.window.mainloop()
