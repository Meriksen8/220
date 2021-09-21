"""
Name: Miles Eriksen
lab4.py

Problem: Graphics

Certification of Authenticity
I certify that this assignment is entirely my own work.
"""

from graphics import *


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Draw a Rectangle")
    win.setCoords(0.0,0.0,10.0,10.0)


    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    shape = Rectangle(p1,p2)
    shape.setFill("Blue")
    shape.setOutline("Blue")
    shape.draw(win)
    message = Text(Point(2.5, 0.5), "Perimeter & Area: ")
    message.draw(win)
    x = p1.getX()
    y = p2.getY()
    message2 = Text(Point(5.5, 0.5), round((y-x)*2 + (x-y)*2,2))
    message2.draw(win)
    message3 = Text(Point(7.0, 0.5),round((y-x * x-y),2))
    message3.draw(win)
    win.getMouse()

    pass

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p1 = win.getMouse()
        c1 = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p1.getX() - c1.getX()
        dy = p1.getY() - c1.getY()
        shape_clone = shape.clone()
        shape_clone.move(dx,dy)
        shape_clone.draw(win)
    instructions.undraw()
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)



    win.getMouse()
    win.close()

def main():
    squares()
    rectangle()
    # circle()
    # pi2()


main()
