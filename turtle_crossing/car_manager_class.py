from turtle import Turtle,Screen
import random
import os

CAR_GIFS = [
    os.path.join(os.path.dirname(__file__), f"car_{color}.gif")
    for color in ["red", "blue", "yellow", "green", "orange", "purple"]
]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager:
    def __init__(self,screen):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        for gif in CAR_GIFS:
            screen.addshape(gif)

    def create_car(self):
        if random.randint(1, 10) == 1:
            new_y = random.randint(-215, 215)
            for car in self.all_cars:
                if car.xcor() > 260 and abs(car.ycor() - new_y) < 28:
                    return
            car = Turtle()
            car.shape(random.choice(CAR_GIFS))
            car.penup()
            car.setheading(180)
            car.goto(300, new_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
        for car in [c for c in self.all_cars if c.xcor() < -320]:
            car.hideturtle()
            self.all_cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT