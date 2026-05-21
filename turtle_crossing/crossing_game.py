import time
from turtle import Screen
from .player_class import Player
from .start_finish_line_class import Line
from .car_manager_class import CarManager
from .scoreboard_class import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title("Turtle Crossing")
    screen.bgcolor("white")
    Line()
    player = Player(screen)
    cars = CarManager(screen)
    scoreboard = Scoreboard()
    screen.listen()
    game_is_on = True
    while game_is_on:
        cars.create_car()
        cars.move_cars()
        time.sleep(0.1)
        screen.update()
        if player.ycor() > 230:
            player.goto((0, -280))
            scoreboard.increase_score()
            cars.increase_speed()
        for car in cars.all_cars:
            if player.distance(car) < 28:
                scoreboard.game_over()
                game_is_on = False
                break
    screen.mainloop()
if __name__ == "__main__":
    main()