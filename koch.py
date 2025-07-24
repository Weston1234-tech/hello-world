import turtle
import math

def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        distance /= 3.0
        drawFractalLine(t, distance, angle, level - 1)
        drawFractalLine(t, distance, angle + 60, level - 1)
        drawFractalLine(t, distance, angle - 60, level - 1)
        drawFractalLine(t, distance, angle, level - 1)

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    level = 3
    length = 300

    t.penup()
    t.goto(-length / 2, length / (2 * math.sqrt(3)))
    t.pendown()

    for angle in [0, -120, 120]:
        drawFractalLine(t, length, angle, level)

    screen.mainloop()
