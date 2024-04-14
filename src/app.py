import pyautogui
import course, tree, ball, club, goal

def reassert_order():
    #course.window.lift()
    goal.window.lift()
    ball.window.lift()
    tree.window.lift()
    club.window.lift()

def periodic_update():
    x, y = pyautogui.position()
    club.rotate_club(x, y, ball.getLocation(), ball.getCurrentState())
    
    # Detect ball
    goal.detect_ball(ball)
    tree.detect_collision_with_ball(ball)
    
    club.window.after(10, periodic_update)
    

if __name__ == '__main__':
    club = club.Club()
    #course = course.Course()
    tree = tree.Tree()
    ball = ball.Ball()
    goal = goal.Goal()

    club.window.bind("<FocusIn>", lambda e: reassert_order())    # Bind the focus in event to reassert order
    #course.window.bind("<FocusIn>", lambda e: reassert_order())
    ball.window.bind("<FocusIn>", lambda e: reassert_order())
    goal.window.bind("<FocusIn>", lambda e: reassert_order())
    reassert_order() # Initial stacking order

    club.window.after(10, periodic_update)
    club.window.mainloop()
