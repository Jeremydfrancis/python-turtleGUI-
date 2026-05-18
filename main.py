import turtle as t
from turtle import Screen, Turtle
import random_walk
import shapes
import circle
import hirst_painting
import event_listeners
import turtle_race
from snake import snake_game


def main():
    try:
        while True:
            user_choice = input("Please select a function to run: "
                  "\n1). Random walk. "
                  "\n2). Draw all shapes."
                  "\n3). Draw a spirograph."
                  "\n4). Draw Hirst Dot Painting."
                  "\n5). Free draw with turtle."
                  "\n6). Turtle Race."
                  "\n7). Snake Game.\n")
            if user_choice not in ["1", "2", "3", "4", "5", "6","7"]:
                print("Please enter a valid option")
                continue
            else:
                break
        if user_choice == "1":
            iterations = int(input("Please enter the number of iterations: "))
            t.colormode(255)
            screen = Screen()
            walk_turtle = Turtle()
            walk_turtle.speed("fastest")
            walk_turtle.pensize(5)
            for _ in range(iterations):
                random_walk.random_walk(walk_turtle)
            screen.exitonclick()
        elif user_choice == "2":
            screen = Screen()
            shape_turtle = Turtle()
            shape_turtle.speed("fastest")
            shape_turtle.shape("turtle")
            shape_turtle.color("green")
            shapes.draw_all_shapes(shape_turtle)
            screen.exitonclick()
        elif user_choice == "3":
            t.colormode(255)
            screen = Screen()
            circle_turtle = Turtle()
            circle_turtle.speed("fastest")
            circle.change_angle(circle_turtle)
            screen.exitonclick()
        elif user_choice == "4":
            t.colormode(255)
            screen = Screen()
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

        print("Program ended")
    except ValueError as e:
        print(f"Program ended: {e}")
if __name__ == "__main__":
    main()

