import turtle as t
import random as r

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color")
colors = ["red", "orange", "pink", "yellow", "green", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. {winning_color} is a winner")
            else:
                print(f"You've lost. {winning_color} is a winner")
        random_distance = r.randint(1, 5)
        turtle.forward(random_distance)

#
# timmy = t.Turtle(shape="turtle")
# timmy.color("red")
# timmy.penup()
# timmy.goto(x=-230, y=-100)
#
# jonny = t.Turtle(shape="turtle")
# jonny.color("yellow")
# jonny.penup()
# jonny.goto(x=-230, y=-70)
#
# anna = t.Turtle(shape="turtle")
# anna.color("pink")
# anna.penup()
# anna.goto(x=-230, y=-40)
#
# tom = t.Turtle(shape="turtle")
# tom.color("green")
# tom.penup()
# tom.goto(x=-230, y=-10)
#
# jack = t.Turtle(shape="turtle")
# jack.color("purple")
# jack.penup()
# jack.goto(x=-230, y=20)

screen.exitonclick()
