from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 0
        self.update_score()
    def update_score(self):
        self.goto(-230,250)
        self.write(f"LEVEL: {self.score}", align="center", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

