import tkinter as tk
import pyautogui
import time
from tree import Tree
from ball import Ball
from club import Club
from goal import Goal
from flag import Flag

class GameController:
    def __init__(self, root):
        self.root = root
        self.max_rounds = 3
        self.max_strokes = 5

        self.current_round = 0
        self.current_stroke = 0
        
        self.goal_hit = False
        self.stroke_taken = False

        self.club = Club()
        self.tree = Tree()
        self.ball = Ball()
        self.goal = Goal()
        self.flag = Flag(self.goal)

        self.setup_bindings()

    def setup_bindings(self):
        self.club.window.bind("<FocusIn>", lambda e: self.reassert_order())
        self.tree.window.bind("<FocusIn>", lambda e: self.reassert_order())
        self.ball.window.bind("<FocusIn>", lambda e: self.reassert_order())
        self.goal.window.bind("<FocusIn>", lambda e: self.reassert_order())
        self.flag.window.bind("<FocusIn>", lambda e: self.reassert_order())

    def reassert_order(self):
        self.goal.window.lift()
        self.flag.window.lift()
        self.ball.window.lift()
        self.tree.window.lift()
        self.club.window.lift()

    def start_game(self):
        self.next_round()

    def next_round(self):
        if self.current_round < self.max_rounds:
            print(f"Starting round {self.current_round}")
            self.current_round += 1
            self.start_round()
        else:
            print("Game over!")
            self.root.destroy()

    def start_round(self):
        self.reset_game_objects()
        self.make_windows_visible(True)
        self.club.window.after(10, self.periodic_update)

    def reset_game_objects(self):
        self.tree.place_tree()
        self.ball.position_ball_in_center()
        self.ball.setVelocity(0,0)
        self.goal.placegoal()
        self.flag.place_flag(self.goal)
        self.current_stroke = 0  # Reset stroke count at the start of each round

    def periodic_update(self):
        if self.current_stroke <= self.max_strokes and not self.goal_hit:
            x, y = pyautogui.position()
            self.club.rotate_club(x, y, self.ball.getLocation(), self.ball.getCurrentState())
            self.goal_hit = self.goal.detect_ball(self.ball)
            self.tree.detect_collision_with_ball(self.ball)
            if self.stroke_taken == False:
                if self.ball.getCurrentState() == "launch":
                    self.current_stroke += 1
                    self.stroke_taken = True
                    print(self.current_stroke)
            else:
                if self.ball.getCurrentState() == "idle":
                    self.stroke_taken = False
 
            self.club.window.after(10, self.periodic_update)
        else:
            self.finish_round()

    def finish_round(self):
        self.goal_hit = False
        self.make_windows_visible(False)  # Make windows invisible immediately when round ends
        self.root.after(5000, self.next_round)  # Delay before starting next round

    def make_windows_visible(self, visible):
        if visible:
            self.club.window.deiconify()
            self.tree.window.deiconify()
            self.ball.window.deiconify()
            self.goal.window.deiconify()
            self.flag.window.deiconify()
        else:
            self.club.window.withdraw()
            self.tree.window.withdraw()
            self.ball.window.withdraw()
            self.goal.window.withdraw()
            self.flag.window.withdraw()

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    game = GameController(root)
    game.start_game()
    root.mainloop()
