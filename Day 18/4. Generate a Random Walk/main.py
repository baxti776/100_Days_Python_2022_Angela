# import turtle as t
# import random
#
# t.speed(0)
# t.pensize(15)
# directions = [90, 180, 270, 0]
# colors = ["dark slate blue", "red", "dark goldenrod", "dark olive green", "navy", "light slate gray", "dodger blue",
#           "magenta"]
# while True:
#     t.color(random.choice(colors))
#     t.forward(30)
#     t.setheading(random.choice(directions))
#
# screen = t.Screen()
# screen.exitonclick()
import turtle as t
import random

t.speed(0)
t.pensize(15)
directions = []
t.colormode(255)
for _ in range(0, 360):
    directions.append(_)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


while True:
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
