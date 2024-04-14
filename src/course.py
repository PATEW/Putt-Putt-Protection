import tkinter as tk

COURSE_IMAGE = './resources/course.png'

class Course:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=COURSE_IMAGE)
        tk.Label(self.window, image=self.image, borderwidth=0).pack(expand=True)
        self.center_window()

    def center_window(self):
        screen_width, screen_height = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        center_x, center_y = (screen_width - self.window.winfo_width()) // 2, (screen_height - self.window.winfo_height()) // 2
        self.window.geometry(f'+{center_x}+{center_y}')
