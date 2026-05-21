from turtle import Turtle, Screen
from .paddle_class import Paddle
import os
import time
from .scoreboard_class import Scoreboard
from .ball_class import Ball


def collision_bool(ball, left_paddle, right_paddle):
    hit_left = (ball.distance(left_paddle) < 50
                and ball.xcor() < -330
                and ball.dx < 0)

    hit_right = (ball.distance(right_paddle) < 50
                 and ball.xcor() > 330
                 and ball.dx > 0)

    return hit_left or hit_right

def main():
    screen = Screen()
    screen.title("Pong")
    screen.setup(800, 700)
    screen.tracer(0)
    screen.bgcolor("black")

    left_paddle = Paddle((-350, 0))
    right_paddle = Paddle((350, 0))

    ball = Ball()
    prompt = Turtle()
    prompt.hideturtle()
    prompt.penup()
    prompt.color("firebrick")
    prompt.goto(0,200)
    prompt.write("Press SPACE to start", align="center", font=("Courier", 40, "bold"))

    started =[False]

    def start_game():
        started[0] = True

    screen.listen()
    screen.onkey(start_game, "space")

    while not started[0]:
        screen.update()
    bg_path = os.path.join(os.path.dirname(__file__), "pong_background.gif")
    screen.addshape(bg_path)
    screen.bgpic(bg_path)
    prompt.clear()

    screen.onkeypress(left_paddle.turn_up, "w")
    screen.onkeypress(left_paddle.turn_down, "s")
    screen.onkeypress(right_paddle.turn_up, "Up")
    screen.onkeypress(right_paddle.turn_down, "Down")

    running = [True]

    def quit_game():
        running[0] = False

    screen.onkey(quit_game, "Escape")
    screen.listen()
    left_score = Scoreboard(-200)
    right_score = Scoreboard(200)
    while running[0]:
        time.sleep(0.026)
        ball.move_ball()
        if collision_bool(ball,left_paddle,right_paddle):
            ball.paddle_collision()
        if ball.xcor() > 384:
            left_score.increase_score()
            ball.goto(0, 0)
            screen.update()
            time.sleep(1)
            ball.dx = -8
        elif ball.xcor() < -384:
            right_score.increase_score()
            ball.goto(0, 0)
            screen.update()
            time.sleep(1)
            ball.dx = 8

        screen.update()
    screen.bye()
if __name__ == "__main__":
    main()