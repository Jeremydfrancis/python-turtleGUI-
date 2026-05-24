from turtle import Turtle
class Time(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.goto(220,250)
        self.time = 600
        self.running = True
        self.update_time()



    def decrease_time(self):
        if self.time > 0 and self.running:
            self.time -= 1
            self.update_time()
        else:
            self.running = False

    def update_time(self):
        seconds = self.time%60
        minutes = self.time//60
        self.clear()
        self.write(f"Time left: {minutes}m {seconds}s", align="center")

    def is_expired(self):
        return self.time <= 0