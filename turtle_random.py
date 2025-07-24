import turtle
import random

t = turtle.Turtle()
t.speed(0)

for _ in range(100):
    t.forward(20)
    t.left(random.choice([0, 90, 180, 270]))

turtle.done()
