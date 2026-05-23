from turtle import Turtle
import os

GIF_FILE = os.path.join(os.path.dirname(__file__), "ninja_turtle.gif")
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 8

class Player(Turtle):
    def __init__(self, screen):
        super().__init__()
        screen.addshape(GIF_FILE)
        self.screen = screen
        self.shape(GIF_FILE)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.screen.onkeypress(self.move_up, "w")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

