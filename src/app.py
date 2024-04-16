import tkinter as tk
import pyautogui
from tree import Tree
from ball import Ball
from club import Club
from goal import Goal
from flag import Flag
from sand import Sand
from water import Water
from gamecontroller import GameController

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    game = GameController(root)
    game.start_game()
    root.mainloop()
