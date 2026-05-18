from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1.15, stretch_len=1.15)
        self.color("chartreuse")
        self.penup()
        self.dx = 8
        self.dy = 5.5

    def move_ball(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

        if self.ycor() > 265:
            self.sety(265)
            self.dy *= -1
        elif self.ycor() < -265:
            self.sety(-265)
            self.dy *= -1

        if self.xcor() > 380:
            self.setx(380)
            self.dx *= -1
        elif self.xcor() < -380:
            self.setx(-380)
            self.dx *= -1
    def paddle_collision(self):
        self.dx *= -1





