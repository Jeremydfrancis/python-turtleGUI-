import turtle as t
from turtle import Screen, Turtle
import random_walk
import shapes
import circle
import hirst_painting
import event_listeners
import turtle_race
from snake import snake_game
from pong import pong_game
from turtle_crossing import crossing_game


def main():
    try:
        while True:
            screen = Screen()
            screen.setup(width=600, height=600)
            user_choice = screen.textinput("Game Launcher",
                "Select a game:\n"
                "1. Random Walk\n"
                "2. Draw All Shapes\n"
                "3. Spirograph\n"
                "4. Hirst Dot Painting\n"
                "5. Free Draw\n"
                "6. Turtle Race\n"
                "7. Snake Game\n"
                "8. Pong\n"
                "9. Turtle Crossing")
            if user_choice not in ["1","2","3","4","5","6","7","8","9"]:
                screen.clear()
                continue
            else:
                screen.clear()
                break

        if user_choice == "1":
            screen = Screen()
            iterations = screen.textinput("Random Walk", "Enter number of iterations:")
            screen.clear()
            screen = Screen()
            t.colormode(255)
            walk_turtle = Turtle()
            walk_turtle.speed("fastest")
            walk_turtle.pensize(5)
            for _ in range(int(iterations)):
                random_walk.random_walk(walk_turtle)
            screen.clear()
            main()
        elif user_choice == "2":
            screen = Screen()
            shape_turtle = Turtle()
            shape_turtle.speed("fastest")
            shape_turtle.shape("turtle")
            shape_turtle.color("green")
            shapes.draw_all_shapes(shape_turtle)
            screen.exitonclick()
        elif user_choice == "3":
            screen = Screen()
            t.colormode(255)
            circle_turtle = Turtle()
            circle_turtle.speed("fastest")
            circle.change_angle(circle_turtle)
            screen.exitonclick()
        elif user_choice == "4":
            screen = Screen()
            t.colormode(255)
            grid_turtle = Turtle()
            grid_turtle.speed("fastest")
            hirst_painting.draw_grid(grid_turtle, screen)
            screen.exitonclick()
        elif user_choice == "5":
            screen = Screen()
            control_turtle = Turtle()
            event_listeners.setup_controls(control_turtle, screen)
            screen.exitonclick()
        elif user_choice == "6":
            screen = Screen()
            turtle_race.race(screen)
            screen.exitonclick()
        elif user_choice == "7":
            snake_game.main()
        elif user_choice == "8":
            pong_game.main()
        elif user_choice == "9":
            crossing_game.main()

        print("Program ended")
    except ValueError as e:
        print(f"Program ended: {e}")

if __name__ == "__main__":
    main()