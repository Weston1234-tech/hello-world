import turtle

def hexagon (t, length):
    """Draws a regular hexagon with the given side length."""
    for _ in range(6):
        t.forward(length)
        t.left(60)
        
def radialHexagons(t, n, length):
    """Draws a radial pattern of n hexagons with the given length."""
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)

t = turtle.Turtle()
t.pensize(2)
t.speed(0)
t.color("blue")

def polygons(t, length):
    from polygons import *

radialHexagons(t, 100, 50)

turtle.done()
