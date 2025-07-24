import turtle

def drawSquare(t, x, y, length):
    """Draws a square with the given turtle t, and upper-left corner point (x, y), and a side's length."""
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for _ in range(4):
        t.forward(length)
        t.left(90)

width = 300
height = 200
using_IDLE = True
colormode = 255

my_turtle = turtle.Turtle()

drawSquare(my_turtle, -100, 100, 150)

turtle.done()
