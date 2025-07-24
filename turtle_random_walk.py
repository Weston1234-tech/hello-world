from turtle import Turtle
import random

def randomWalk(t, turns, distance = 20):
    """Turns a random number of degrees and moves a given distance for a fixed number of turms."""
    for x in range(turns):
        degrees = random.randint(0, 270)
        if x % 2 == 0:
            t.left(degrees)
        else:
            t.right(degrees)
        t.forward(distance)


def main():
        t = Turtle()
        t.shape("turtle")
        t.speed(0)
        randomWalk(t, 40, 30)

if __name__ == "__main__":
        main()
