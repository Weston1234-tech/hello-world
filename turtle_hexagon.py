import turtle
def hexagon(t, length):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left(60)

t = turtle.Turtle()
t.pensize(2)
t.speed(3)
t.color("blue")
hexagon(t, 100)

turtle.done()
