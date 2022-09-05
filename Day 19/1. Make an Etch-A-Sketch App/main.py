import turtle as t

screen = t.Screen()


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def setHeadingLeft():
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def setHeadingRight():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def clear():
    t.penup()
    t.clear()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(setHeadingRight, "d")
screen.onkey(setHeadingLeft, "a")
screen.onkey(clear, "c")

screen.exitonclick()
