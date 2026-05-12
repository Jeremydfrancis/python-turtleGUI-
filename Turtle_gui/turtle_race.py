import random
from turtle import Turtle

def create_turtles():
    colors = ["blue", "red", "orange", "yellow", "green", "pink"]
    turtles = {}
    counter = -175
    for color in colors:
        turtles[color] = Turtle()
        turtles[color].color(color)
        turtles[color].penup()
        turtles[color].shape("turtle")
        counter += 50
        turtles[color].speed(0)
        turtles[color].goto(-200, counter)
        turtles[color].speed(5)
    return turtles

def create_finish_line():
    line_turtle = Turtle()
    line_turtle.speed(0)
    line_turtle.penup()
    line_turtle.hideturtle()
    line_turtle.goto(165, 175)
    line_turtle.pendown()
    line_turtle.goto(165, -175)
    finish_txt = "F,I,N,I,S,H".split(",")
    y_axis = 155
    x_axis = 190
    line_turtle.color("cyan")
    for letter in finish_txt:
        line_turtle.penup()
        line_turtle.goto(x_axis, y_axis)
        line_turtle.write(f"{letter}", align="center", font=("Arial", 16, "bold"))
        y_axis -= 66

def get_bet(screen):
    while True:
        try:
            user_bet = screen.textinput("Turtle Race", 'Which turtle will win?\n(blue, red, orange, yellow, green, pink)')
            if user_bet is None:
                continue
            user_bet = user_bet.strip().lower()
            if user_bet in ["blue", "red", "orange", "yellow", "green", "pink"]:
                return user_bet
        except AttributeError:
            continue

def check_winner(turtles):
    for color, turtle in turtles.items():
        if turtle.xcor() >= 165:
            return f"{color.upper()} WINS"
    return None

def random_steps(turtles):
    for color, turtle in turtles.items():
        turtle.forward(random.randint(1, 10))

def display_winner(winner, bet):
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0, 0)
    if bet.upper() in winner:
        result_turtle.color("white")
        result_turtle.write(f"You won! {winner}", align="center", font=("Arial", 16, "bold"))
    else:
        result_turtle.color("red")
        result_turtle.write(f"You lost! {winner}", align="center", font=("Arial", 16, "bold"))
def race(screen):
    screen.setup(width=500, height=400)
    screen.bgcolor("grey")

    turtles = create_turtles()
    create_finish_line()
    bet = get_bet(screen)

    winner = None
    while winner is None:
        random_steps(turtles)
        winner = check_winner(turtles)

    if bet.upper() in winner:
        print(f"You won! {winner}")
    else:
        print(f"You lost! {winner}")
    display_winner(winner, bet)