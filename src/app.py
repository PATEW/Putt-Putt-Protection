import pyautogui
import course, tree, ball, club, goal, sand, water

def reassert_order():
    #course.window.lift()
   
    sand.window.lift()
    water.window.lift()
    tree.window.lift()
    goal.window.lift()
    ball.window.lift()
    club.window.lift()

def periodic_update():
    x, y = pyautogui.position()
    club.rotate_club(x, y, ball.getLocation(), ball.getCurrentState())
    club.window.after(1, periodic_update)
    # Detect ball
    goal.detect_ball(ball)
    sand.detect_collision_with_ball(ball)
    water.detect_collision_with_ball(ball)
    tree.detect_collision_with_ball(ball)  

if __name__ == '__main__':
    club = club.Club()
    tree = tree.Tree() 
    sand = sand.Sand()
    water = water.Water()
    goal = goal.Goal()
    ball = ball.Ball()
    
    

    club.window.bind("<FocusIn>", lambda e: reassert_order())    # Bind the focus in event to reassert order
    ball.window.bind("<FocusIn>", lambda e: reassert_order())
    tree.window.bind("<FocusIn>", lambda e: reassert_order())
    sand.window.bind("<FocusIn>", lambda e: reassert_order())
    water.window.bind("<FocusIn>", lambda e: reassert_order())
    goal.window.bind("<FocusIn>", lambda e: reassert_order())
    reassert_order() # Initial stacking order

    club.window.after(10, periodic_update)
    club.window.mainloop()
