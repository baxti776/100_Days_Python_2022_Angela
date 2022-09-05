from turtle import *
from random import choice

t = Turtle()
t.speed(100)
colors = ["dark slate blue", "red", "dark goldenrod", "dark olive green", "navy"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


shapes = 2
while True:
    t.color(choice(colors))
    shapes += 1
    draw_shape(shapes)

screen = Screen()
screen.exitonclick()
