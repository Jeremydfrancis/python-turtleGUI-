from turtle import Screen
import time
import os
from snake import snake_class
from snake.food_class import Food
from snake.scoreboard_class import Scoreboard
from snake.game_prompt_class import Prompt


class GameExit(Exception):
    pass

def main():
    screen = Screen()
    screen.title("Snake Game")
    bg_path = os.path.join(os.path.dirname(__file__), "snake_bg.gif")
    screen.bgpic(bg_path)
    screen.setup(600, 600)
    screen.tracer(0)
    prompt = Prompt()
    scoreboard = Scoreboard()
    scoreboard.load_highscore()
    escaped = [False]
    def on_escape():
        escaped[0] = True
    screen.listen()
    screen.onkey(on_escape, "Escape")

    def wait_for_space():
        ready = [False]
        def on_space():
            ready[0] = True
        screen.onkey(on_space, "space")
        while not ready[0]:
            if escaped[0]:
                raise GameExit
            screen.update()
        prompt.clear()

    try:
        wait_for_space()

        snake = snake_class.Snake(screen)
        food = Food()

        while True:
            time.sleep(0.1)
            screen.update()

            if escaped[0]:
                raise GameExit

            snake.move()

            if snake.head.distance(food) < 15:
                food.refresh()
                snake.extend_snake()
                scoreboard.increase_score()

            if snake.is_out_of_bounds() or snake.is_hitting_self():
                scoreboard.reset_score()
                snake.reset_snake()
                prompt.show()
                screen.update()
                wait_for_space()

    except GameExit:
        scoreboard.save_highscore()
        screen.clear()


if __name__ == "__main__":
    main()