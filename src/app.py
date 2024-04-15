import pyautogui
import tree, ball, club, goal, flag

def reassert_order():
    goal.window.lift()
    flag.window.lift()
    ball.window.lift()
    tree.window.lift()
    club.window.lift()

def periodic_update():
    if not goal.game_over:  # Only update if the game isn't over
        x, y = pyautogui.position()
        club.rotate_club(x, y, ball.getLocation(), ball.getCurrentState())
        
        # Detect ball
        goal.detect_ball(ball)
        tree.detect_collision_with_ball(ball)
        
        club.window.after(10, periodic_update)
    else:
        # Cleanly exit the program
        club.window.destroy()  # This closes the main application window and all children

    

if __name__ == '__main__':
    club = club.Club()
    tree = tree.Tree()
    ball = ball.Ball()
    goal = goal.Goal()
    flag = flag.Flag(goal)

    club.window.bind("<FocusIn>", lambda e: reassert_order())    # Bind the focus in event to reassert order
    tree.window.bind("<FocusIn>", lambda e: reassert_order())
    ball.window.bind("<FocusIn>", lambda e: reassert_order())
    goal.window.bind("<FocusIn>", lambda e: reassert_order())
    flag.window.bind("<FocusIn>", lambda e: reassert_order())
    reassert_order() # Initial stacking order

    club.window.after(10, periodic_update)
    club.window.mainloop()
