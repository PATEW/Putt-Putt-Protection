import tkinter as tk
import math

BALL_IMAGE = './resources/ball.png'
DECELERATION_RATE = 0.1
CURRENT_STATE = "idle"
START_LOCATION = (0, 0)

class Ball:
    def __init__(self):
        self.is_dragging = False
        self.start_x = self.start_y = self.drag_start_x = self.drag_start_y = self.velocity_x = self.velocity_y = 0
        self.deceleration_rate = DECELERATION_RATE
        self.current_state = CURRENT_STATE
        self.start_location = START_LOCATION
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.wm_attributes("-transparentcolor", "white", "-topmost", True)
        self.image = tk.PhotoImage(file=BALL_IMAGE)
        self.ball = tk.Label(self.window, image=self.image, borderwidth=0)
        self.ball.pack()
        self.bind_events()
        self.position_ball_in_center()

    def bind_events(self):
        self.ball.bind("<Button-1>", self.start_drag)
        self.ball.bind("<B1-Motion>", self.on_drag)
        self.ball.bind("<ButtonRelease-1>", self.end_drag)

    def position_ball_in_center(self):
        screen_width, screen_height = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        center_x, center_y = (screen_width - self.ball.winfo_reqwidth()) // 2, (screen_height - self.ball.winfo_reqheight()) // 2
        self.window.geometry(f'+{center_x}+{center_y}')

    def start_drag(self, event):
        self.current_state = "start"
        self.is_dragging = True
        self.start_x, self.start_y = event.x_root, event.y_root
        self.drag_start_x, self.drag_start_y = self.start_x, self.start_y  # Capture initial drag position

    def on_drag(self, event):
        self.current_state = "drag"
        if not self.is_dragging:
            return
        self.start_location = self.window.winfo_x(), self.window.winfo_y()
        delta_x, delta_y = event.x_root - self.start_x, event.y_root - self.start_y
        new_x, new_y = self.window.winfo_x() + delta_x, self.window.winfo_y() + delta_y
        self.start_x, self.start_y = event.x_root, event.y_root

    def end_drag(self, event):
        self.current_state = "end"
        self.is_dragging = False
        # Calculate the opposite velocity
        self.velocity_x = (self.drag_start_x - event.x_root) / 10
        self.velocity_y = (self.drag_start_y - event.y_root) / 10
        self.launch_ball()
        


    def launch_ball(self):
        self.current_state = "launch"
        screen_width, screen_height = self.window.winfo_screenwidth(), self.window.winfo_screenheight()

        # Apply deceleration to the velocity vector as a whole
        magnitude = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        decelerated_magnitude = max(0, magnitude - self.deceleration_rate)
        
        # Scale the velocity components proportionally to the new magnitude
        if decelerated_magnitude > 0 and magnitude > 0:
            scale_factor = decelerated_magnitude / magnitude
            self.velocity_x *= scale_factor
            self.velocity_y *= scale_factor
        else:
            self.current_state = "idle"
            self.velocity_x = 0
            self.velocity_y = 0
            return
            
            

        # Update positions with boundary checks
        new_x = min(max(0, self.window.winfo_x() + self.velocity_x), screen_width - self.ball.winfo_width())
        new_y = min(max(0, self.window.winfo_y() + self.velocity_y), screen_height - self.ball.winfo_height())

        # Reverse direction on hitting boundaries
        if new_x in (0, screen_width - self.ball.winfo_width()):
            self.velocity_x = -self.velocity_x
        if new_y in (0, screen_height - self.ball.winfo_height()):
            self.velocity_y = -self.velocity_y

        self.window.geometry(f'+{int(new_x)}+{int(new_y)}')
        self.window.after(10, self.launch_ball)

    def getLocation(self):
        return self.window.winfo_x(), self.window.winfo_y()
    
    def getDimensions(self):
        return self.ball.winfo_width(), self.ball.winfo_height()

    def getCurrentState(self):
        return self.current_state
    
    def getStartLocation(self):
        return self.start_location
    
    def stop_ball(self):
        self.current_state = "idle"
        self.velocity_x = 0
        self.velocity_y = 0       

    def setVelocity(self, x, y):
        self.velocity_x = x
        self.velocity_y = y
        return
    
    def getCurrentVelocity(self):
        return math.sqrt(self.velocity_x**2 + self.velocity_y**2)

