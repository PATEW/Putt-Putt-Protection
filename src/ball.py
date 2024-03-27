import tkinter as tk
import pyautogui
import math

BALL_IMAGE = './resources/ball.png'
DECELERATION_RATE = 0.1

class Ball:
    def __init__(self):
        self.is_dragging = False
        self.start_x = 0
        self.start_y = 0
        self.drag_start_x = 0  # Initial drag position for velocity calculation
        self.drag_start_y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.deceleration_rate = DECELERATION_RATE

        self.ball_window = tk.Toplevel()
        self.ball_window.overrideredirect(True)
        self.ball_window.wm_attributes("-transparentcolor", "white")
        self.ball_window.wm_attributes("-topmost", True)

        self.ball_image = tk.PhotoImage(file=BALL_IMAGE)
        self.ball = tk.Label(self.ball_window, image=self.ball_image, borderwidth=0)
        self.ball.pack()

        self.ball.bind("<Button-1>", self.start_drag)
        self.ball.bind("<B1-Motion>", self.on_drag)
        self.ball.bind("<ButtonRelease-1>", self.end_drag)

        self.position_ball_in_center()

    def position_ball_in_center(self):
        screen_width = self.ball_window.winfo_screenwidth()
        screen_height = self.ball_window.winfo_screenheight()
        center_x = int(screen_width / 2 - self.ball.winfo_reqwidth() / 2)
        center_y = int(screen_height / 2 - self.ball.winfo_reqheight() / 2)
        self.ball_window.geometry(f'+{center_x}+{center_y}')

    def start_drag(self, event):
        self.is_dragging = True
        self.start_x, self.start_y = event.x_root, event.y_root
        self.drag_start_x, self.drag_start_y = event.x_root, event.y_root  # Capture initial drag position

    def on_drag(self, event):
        if self.is_dragging:
            delta_x = event.x_root - self.start_x
            delta_y = event.y_root - self.start_y
            new_x = self.ball_window.winfo_x() + delta_x
            new_y = self.ball_window.winfo_y() + delta_y

            self.start_x, self.start_y = event.x_root, event.y_root

            self.ball_window.geometry(f'+{int(new_x)}+{int(new_y)}')

    def end_drag(self, event):
        self.is_dragging = False
        end_x, end_y = event.x_root, event.y_root
        self.velocity_x = (end_x - self.drag_start_x) / 10
        self.velocity_y = (end_y - self.drag_start_y) / 10

        self.launch_ball()

    def launch_ball(self):
        screen_width = self.ball_window.winfo_screenwidth()
        screen_height = self.ball_window.winfo_screenheight()

        # Calculate the magnitude of the velocity vector
        velocity_magnitude = math.sqrt(self.velocity_x**2 + self.velocity_y**2)

        # Apply deceleration to the magnitude
        velocity_magnitude = max(0, velocity_magnitude - self.deceleration_rate)

        # Calculate new velocities while maintaining direction
        if velocity_magnitude > 0:
            scale_factor = velocity_magnitude / math.sqrt(self.velocity_x**2 + self.velocity_y**2)
            self.velocity_x *= scale_factor
            self.velocity_y *= scale_factor
        else:
            self.velocity_x = 0
            self.velocity_y = 0

        # Update positions
        new_x = self.ball_window.winfo_x() + self.velocity_x
        new_y = self.ball_window.winfo_y() + self.velocity_y

        # Boundary checks
        if new_x < 0:
            new_x = 0
            self.velocity_x = -self.velocity_x  # Reverse direction on hitting left boundary
        elif new_x > screen_width - self.ball.winfo_width():
            new_x = screen_width - self.ball.winfo_width()
            self.velocity_x = -self.velocity_x  # Reverse direction on hitting right boundary

        if new_y < 0:
            new_y = 0
            self.velocity_y = -self.velocity_y  # Reverse direction on hitting top boundary
        elif new_y > screen_height - self.ball.winfo_height():
            new_y = screen_height - self.ball.winfo_height()
            self.velocity_y = -self.velocity_y  # Reverse direction on hitting bottom boundary

        self.ball_window.geometry(f'+{int(new_x)}+{int(new_y)}')
        self.ball_window.after(10, self.launch_ball)

    def apply_deceleration(self, velocity):
            """Apply deceleration to the velocity."""
            if velocity > 0:
                return max(0, velocity - self.deceleration_rate)
            elif velocity < 0:
                return min(0, velocity + self.deceleration_rate)
            return 0