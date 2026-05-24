from turtle import Turtle

class State(Turtle):
    def __init__(self,state,coordinates):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(coordinates)
        self.write(state,font=("Arial",10,"bold"),align = "center")
