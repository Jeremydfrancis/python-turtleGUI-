from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self,screen):
        self.screen = screen
        self.all_segments = []
        self.head = None
        self.setup()
        self.screen.listen()
        self.screen.onkey(self.turn_up, "Up")
        self.screen.onkey(self.turn_down, "Down")
        self.screen.onkey(self.turn_left, "Left")
        self.screen.onkey(self.turn_right, "Right")

    def setup(self):
        self.create_snake()
        self.head = self.all_segments[0]
        self.head.color("Red")
        self.head.shape("triangle")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        segment = Turtle()
        segment.penup()
        segment.speed(2)
        segment.shape("square")
        segment.color("white")
        segment.goto(position)
        self.all_segments.append(segment)
    def extend_snake(self):
        self.add_segment(self.all_segments[-1].position())

    def reset_snake(self):
        for seg in self.all_segments:
            seg.hideturtle()
        self.all_segments.clear()
        self.setup()

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def is_hitting_self(self):
        for segment in self.all_segments[1:]:
            if self.head.distance(segment) < 7:
                return True
        return False

    def is_out_of_bounds(self):
        return (self.head.xcor() > 280 or self.head.xcor() < -280 or
                self.head.ycor() > 280 or self.head.ycor() < -280)

    def move(self):
        for segment in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[segment - 1].xcor()
            new_y = self.all_segments[segment - 1].ycor()
            self.all_segments[segment].goto(new_x, new_y)
        self.all_segments[0].forward(20)
