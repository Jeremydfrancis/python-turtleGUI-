from turtle import Turtle

class Prompt(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write("Press SPACE to start", align="center", font=("Courier", 20, "bold"))

    def show(self):
        message = "Press SPACE to continue  |  ESC to quit"
        self.clear()
        self.write(message, align="center", font=("Courier", 20, "bold"))