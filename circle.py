import turtle
import math

def drawCircle(t, centerX, centerY, radius):
    t.penup()
    t.goto(centerX + radius, centerY)
    t.setheading(90)
    t.pendown()

    step_length = 2.0 * math.pi * radius / 120.0

    for _ in range(120):
        t.forward(step_length)
        t.right(3)

if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()

    drawCircle(t, 0, 0, 100)

    screen.mainloop()
