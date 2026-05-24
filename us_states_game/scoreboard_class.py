from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.sety(245)
        self.write(f"Score:{self.score}/50", align="center", font=("Courier", 20, "bold"))

    def game_over(self):
        self.sety(0)
        self.color("red")
        self.write(f"GAME OVER\nFinal Score\n{self.score}/50", align="center", font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()