from us_states_game.time_class import Time
from turtle import Screen
from us_states_game.state_class import State
from us_states_game.scoreboard_class import Scoreboard
import pandas as pd
import os

def main():
    def load_states():
        data_path = os.path.join(os.path.dirname(__file__), "50_states.csv")
        get_data = pd.read_csv(data_path)
        return get_data.set_index("state").to_dict(orient="index")

    def tick():
        timer.decrease_time()
        screen.update()
        if timer.is_expired():
            score.game_over()
            screen.update()
            return False
        else:
            screen.ontimer(tick, 1000)
            return True

    screen = Screen()
    screen.setup(width=700, height=550)
    screen.bgcolor("black")
    screen.title("US States Game")
    screen.tracer(0)
    timer = Time()
    score = Scoreboard()
    bg_path = os.path.join(os.path.dirname(__file__), "blank_states_img.gif")
    screen.bgpic(bg_path)
    states = load_states()
    tick()

    while True:
        user_answer = screen.textinput(title=f"Guess a state - {score.score}/50", prompt="Name a state:")
        if user_answer is None:
            break
        user_answer = user_answer.strip().title()
        if user_answer in states:
            state = states.pop(user_answer)
            State(user_answer, (state["x"], state["y"]))
            score.increase_score()
            screen.update()
            if len(states) == 0:
                score.game_over()
                screen.update()
                break

    screen.clear()