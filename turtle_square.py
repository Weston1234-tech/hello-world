import turtle

def square(t, length):
    """Draws a square with the given length."""
    for count in range(4):
        t.forward(length)
        t.left(90)

t = turtle.Turtle()
t.pensize(3)
t.speed(2)
t.color("green")

square(t, 100)

turtle.done()
