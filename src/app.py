import tkinter as tk
from gamecontroller import GameController

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    game = GameController(root)
    game.start_game()
    root.mainloop()
