

def setup_controls(turtle, screen):
    def forward():
        turtle.forward(10)

    def backward():
        turtle.backward(10)

    def turn_left():
        turtle.setheading(turtle.heading() + 10)

    def turn_right():
        turtle.setheading(turtle.heading() - 10)

    def clear_screen():
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    screen.listen()
    screen.onkey(forward, "Up")
    screen.onkey(backward, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(clear_screen, "c")