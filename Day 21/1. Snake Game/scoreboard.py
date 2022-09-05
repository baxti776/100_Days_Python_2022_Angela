import turtle
from turtle import Turtle

ALIGN = "center"
FONT = ('Courier ', 25, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.initial_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.initial_score += 1
        self.clear()
        self.update_scoreboard()
