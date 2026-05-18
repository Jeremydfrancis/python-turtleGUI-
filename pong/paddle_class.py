from turtle import Turtle
STARTING_POSITIONS = [(-350, 0),(350,0)]

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
        self.color("cyan")
        self.goto(position)

    def turn_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def turn_down(self):
        new_y = self.ycor() - 15
        self.goto(self.xcor(), new_y)


