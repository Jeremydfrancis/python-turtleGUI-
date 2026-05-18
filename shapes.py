def dashed_line(turtle, dash, segments):
    for _ in range(segments):
        turtle.forward(dash)
        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()

def solid_line(turtle, dash, segments):
    for _ in range(segments):
        turtle.forward(dash)

def create_shape(turtle, line_type, sides):
    angle = 360 / sides
    for _ in range(sides):
        line_type()
        turtle.left(angle)

def draw_triangle(turtle, line_type):
    create_shape(turtle, line_type, sides=3)

def draw_square(turtle, line_type):
    create_shape(turtle, line_type, sides=4)

def draw_pentagon(turtle, line_type):
    create_shape(turtle, line_type, sides=5)

def draw_hexagon(turtle, line_type):
    create_shape(turtle, line_type, sides=6)

def draw_heptagon(turtle, line_type):
    create_shape(turtle, line_type, sides=7)

def draw_octagon(turtle, line_type):
    create_shape(turtle, line_type, sides=8)

def draw_nonagon(turtle, line_type):
    create_shape(turtle, line_type, sides=9)

def draw_decagon(turtle, line_type):
    create_shape(turtle, line_type, sides=10)

def draw_all_shapes(turtle):
    draw_triangle(turtle, lambda: dashed_line(turtle, 5, 10))
    draw_square(turtle, lambda: solid_line(turtle, 5, 10))
    draw_pentagon(turtle, lambda: dashed_line(turtle, 5, 10))
    draw_hexagon(turtle, lambda: solid_line(turtle, 5, 10))
    draw_heptagon(turtle, lambda: dashed_line(turtle, 5, 10))
    draw_octagon(turtle, lambda: solid_line(turtle, 5, 10))
    draw_nonagon(turtle, lambda: dashed_line(turtle, 5, 10))
    draw_decagon(turtle, lambda: solid_line(turtle, 5, 10))