from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.highscore = self.load_highscore()
        self.update_score()
    def update_score(self):
        self.clear()
        self.sety(260)
        self.write(f"Score:{self.score} High Score: {self.highscore}", align="center", font=("Courier", 24, "bold"))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    def game_over(self):
        self.sety(0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()
    def save_highscore(self):
        path = os.path.join(os.path.dirname(__file__), "highscore.txt")
        with open(path, "w") as file:
            file.write(f"{self.highscore}")
    def load_highscore(self):
        path = os.path.join(os.path.dirname(__file__), "highscore.txt")
        try:
            with open(path, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
