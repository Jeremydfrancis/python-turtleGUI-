import random

def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_color():
    return rgb()

def random_direction(turtle):
    direction = [90, 180, 270, 360]
    turtle.setheading(random.choice(direction))

def random_walk(turtle):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.dot(12)
    random_direction(turtle)