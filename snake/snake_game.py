from turtle import Screen, Turtle
import time
import os
from snake import snake_class
from snake.food_class import Food
from snake.scoreboard_class import Scoreboard

def main():
    screen = Screen()
    screen.title("Snake Game")
    bg_path = os.path.join(os.path.dirname(__file__), "snake_bg.gif")
    screen.bgpic(bg_path)
    screen.setup(600, 600)
    screen.tracer(0)
    prompt = Turtle()
    prompt.hideturtle()
    prompt.penup()
    prompt.color("white")
    prompt.write("Press SPACE to start", align="center", font=("Courier", 20, "bold"))
    screen.update()

    started = [False]
    def start_game():
        started[0] = True

    screen.listen()
    screen.onkey(start_game, "space")

    while not started[0]:
        screen.update()

    prompt.clear()

    snake = snake_class.Snake(screen)
    food = Food()
    scoreboard = Scoreboard()

    alive = True
    while alive:
        time.sleep(0.1)
        screen.update()
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()
        if snake.is_out_of_bounds() or snake.is_hitting_self():
            scoreboard.game_over()
            alive = False

    screen.exitonclick()

if __name__ == "__main__":
    main()