from us_states_game.time_class import Time
from us_states_game.state_class import State
from us_states_game.scoreboard_class import Scoreboard
from turtle import Screen
import pandas as pd
import tkinter as tk
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
            game_active[0] = False
            score.game_over()
            screen.update()
        else:
            screen.ontimer(tick, 1000)

    def custom_input(title, prompt):
        result = [None]
        root = screen.getcanvas().winfo_toplevel()
        root_x = root.winfo_x() + root.winfo_width() + 10
        root_y = root.winfo_y() + root.winfo_height() // 2 - 80

        dialog = tk.Toplevel(root)
        dialog.title("")
        dialog.geometry(f"300x160+{root_x}+{root_y}")
        dialog.configure(bg="black")
        dialog.resizable(False, False)

        tk.Label(dialog, text=title, fg="yellow", bg="black",
                 font=("Courier", 11, "bold")).pack(pady=(12, 2))
        tk.Label(dialog, text=prompt, fg="white", bg="black",
                 font=("Courier", 10)).pack()

        entry = tk.Entry(dialog, font=("Courier", 12), bg="#222222",
                         fg="yellow", insertbackground="yellow",
                         relief="flat", width=22)
        entry.pack(pady=8)
        entry.focus()

        def submit(event=None):
            result[0] = entry.get()
            dialog.destroy()

        def check_active():
            if not game_active[0]:
                dialog.destroy()
            else:
                dialog.after(100, check_active)

        entry.bind("<Return>", submit)
        tk.Button(dialog, text="Submit", command=submit, bg="#333333",
                  fg="yellow", font=("Courier", 10, "bold"),
                  relief="flat", width=10).pack()
        dialog.after(100, check_active)
        dialog.wait_window()
        return result[0]


    screen = Screen()
    screen.setup(width=700, height=550)
    screen.bgcolor("black")
    screen.title("US States Game")
    screen.tracer(0)

    timer = Time()
    score = Scoreboard()
    screen.bgpic(os.path.join(os.path.dirname(__file__), "blank_states_img.gif"))
    states = load_states()
    game_active = [True]
    tick()

    # Game loop
    while game_active[0]:
        user_answer = custom_input(f"Guess a state - {score.score}/50", "Name a state:")
        if user_answer is None or not game_active[0]:
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