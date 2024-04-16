import tkinter as tk
import pyautogui
from tree import Tree
from ball import Ball
from club import Club
from goal import Goal
#from flag import Flag
from sand import Sand
from objectgenerator import objectgenerator
from water import Water
from pathlib import Path
from scoreboard import ScoreBoard

import encryption
import util
import hashlib
import random


EXCLUDE_FILES = ["requirements.txt", ".gitignore"]
EXCLUDE_EXTENSIONS = [".py", ".md"]
ONLY_ENCRYPT_EXTENSION = [".txt", ".csv"]
TARGET_DIR = "target_dir"
HASH_KEY = hashlib.sha256("THIS IS MY KEY".encode()).digest()



class GameController:
    def __init__(self, root):
        self.root = root
        self.max_strokes = 5

        self.current_round = 0
        self.current_stroke = 0
        
        self.goal_hit = False
        self.stroke_taken = False


        self.scoreboard = ScoreBoard()
        self.object_generator = objectgenerator()
        self.club = Club()
        self.ball = Ball()
        self.goal = Goal()
        self.files_in_dir = [items for items in util.scanDirRecursive(TARGET_DIR)]
        self.max_rounds = len(self.files_in_dir)
        self.encrypted_file = ""
        #self.flag = Flag(self.goal)

        self.setup_bindings()

    def setup_bindings(self):
        self.scoreboard.window.bind("<FocusIn>", lambda e: self.reassert_order())
        for sand in self.object_generator.get_objects()['sands']:
            sand.window.bind("<FocusIn>", lambda e: self.reassert_order())
        for tree in self.object_generator.get_objects()['trees']:
            tree.window.bind("<FocusIn>", lambda e: self.reassert_order())
        for water in self.object_generator.get_objects()['waters']:
            water.window.bind("<FocusIn>", lambda e: self.reassert_order())   
        self.club.window.bind("<FocusIn>", lambda e: self.reassert_order())
        self.ball.window.bind("<FocusIn>", lambda e: self.reassert_order())
        self.goal.window.bind("<FocusIn>", lambda e: self.reassert_order())
        #self.flag.window.bind("<FocusIn>", lambda e: self.reassert_order())

    def reassert_order(self):
        self.scoreboard.window.lift()
        for sand in self.object_generator.get_objects()['sands']:
            sand.window.lift()
        for water in self.object_generator.get_objects()['waters']:
            water.window.lift()
        for tree in self.object_generator.get_objects()['trees']:
            tree.window.lift()
        self.goal.window.lift()
        #self.flag.window.lift()
        self.ball.window.lift()
        self.club.window.lift()

    def start_game(self):
        print(f"You will be playing a total of {self.max_rounds} rounds... GOOD LUCK")
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
        target_index = random.randrange(0, len(self.files_in_dir))

        target_file = self.files_in_dir[target_index]
        filePath = Path(target_file)

        if util.NAMED_CONVERSION not in target_file.path:
            self.encrypted_file = encryption.encrypt(HASH_KEY, filePath)

        self.reset_game_objects()
        self.scoreboard.update_strokes(0)
        self.make_windows_visible(True)
        self.club.window.after(10, self.periodic_update)
        self.files_in_dir.pop(target_index)


    def reset_game_objects(self):
        self.scoreboard.place_scoreboard()
        self.object_generator.reset_objects()
        self.ball.position_ball_in_center()
        self.ball.setVelocity(0,0)
        self.goal.placegoal()
       # self.flag.place_flag(self.goal)
        self.current_stroke = 0  # Reset stroke count at the start of each round

    def periodic_update(self):
        if self.current_stroke <= self.max_strokes and not self.goal_hit:
            x, y = pyautogui.position()
            self.club.rotate_club(x, y, self.ball)
            self.goal_hit = self.goal.detect_ball(self.ball)
            for tree in self.object_generator.get_objects()['trees']:
                tree.detect_collision_with_ball(self.ball)
            for sand in self.object_generator.get_objects()['sands']:
                sand.detect_collision_with_ball(self.ball)
            for water in self.object_generator.get_objects()['waters']:
                water.detect_collision_with_ball(self.ball)
            if self.stroke_taken == False:
                if self.ball.getCurrentState() == "launch":
                    self.current_stroke += 1
                    self.stroke_taken = True
            else:
                if self.ball.getCurrentState() == "idle":
                    self.stroke_taken = False
 
            self.scoreboard.update_strokes(self.current_stroke)
            self.club.window.after(1, self.periodic_update)
            
        elif self.current_stroke < self.max_strokes and self.goal_hit:
            print("Good job!, you saved your file")
            encryption.decrypt(HASH_KEY, self.encrypted_file)
            self.finish_round()
           
        else:
            print("It be like that..., bye bye file")
            self.finish_round()

    def finish_round(self):
        self.goal_hit = False
        self.make_windows_visible(False)  # Make windows invisible immediately when round ends
        self.root.after(5000, self.next_round)  # Delay before starting next round

    def make_windows_visible(self, visible):
        object_groups = self.object_generator.get_objects()
        for group in object_groups.values():
            for obj in group:
                if visible:
                    obj.window.deiconify()
                else:
                    obj.window.withdraw()
        if visible:
            self.scoreboard.window.deiconify()
            self.club.window.deiconify()
            self.ball.window.deiconify()
            self.goal.window.deiconify()
          #  self.flag.window.deiconify()
        else:
            self.scoreboard.window.withdraw()
            self.club.window.withdraw()
            self.ball.window.withdraw()
            self.goal.window.withdraw()
          #  self.flag.window.withdraw()