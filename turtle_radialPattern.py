import turtle

def triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.left(120)

def radialPattern(t, n, length, shape):
    """Draws a radial pattern of n shapes with the given length."""
    for count in range(n):
        shape(t, length)
        t.left(360 / n)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("blue")

radialPattern(t, 12, 100, triangle)

turtle.done()
