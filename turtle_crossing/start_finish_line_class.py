from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.starting_line()
        self.finish_line()

    def starting_line(self):
        self.goto(-310, -230)
        self.pendown()
        self.color("green")
        self.goto(310, -230)
        self.penup()
        self.goto(200, -280)
        self.write('START', align="center", font=FONT)

    def finish_line(self):
        self.color("red")
        self.goto(-310, 230)
        self.pendown()
        self.goto(310, 230)
        self.penup()
        self.goto(200, 250)
        self.write('FINISH', align="center", font=FONT)

