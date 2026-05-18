from random_walk import random_color

def create_circle(turtle):
    turtle.color(random_color())
    turtle.circle(100)

def change_angle(turtle):
    start_angle = 0
    end_angle = 360
    while start_angle <= end_angle:
        start_angle += 1
        create_circle(turtle)
        turtle.setheading(turtle.heading() + start_angle)