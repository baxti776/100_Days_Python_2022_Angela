import turtle as t
import random

t.width(1)
heading = 0
t.colormode(255)
t.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


while True:
    heading += 10
    t.color(random_color())
    t.setheading(heading)
    t.circle(100)

screen = t.Screen()
screen.exitonclick()
