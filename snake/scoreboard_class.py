from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.update_score()
    def update_score(self):
        self.sety(260)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 24, "bold"))
    def game_over(self):
        self.sety(0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
