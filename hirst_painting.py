from random_walk import random_color

def draw_grid(turtle, screen):
    width = screen.window_width()
    height = screen.window_height()

    dot_size = 20
    spacing = 30
    columns = width // spacing
    rows = height // spacing

    turtle.penup()
    turtle.goto(-width // 2 + 10, -height // 2 + 20)

    def move_turtle():
        turtle.penup()
        turtle.color(random_color())
        turtle.dot(dot_size)
        turtle.forward(spacing)


    def new_line():
        position = list(turtle.position())
        position[0] = -width // 2 + 10
        position[1] += spacing
        turtle.goto(tuple(position))

    for i in range(rows):
        for j in range(int(columns)):
            move_turtle()
        new_line()