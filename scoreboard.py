from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0

    def display(self):
        self.write(self.score, align="center", font=("Courier", 80, "normal"))


class MiddleLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.goto(0, -300)

    def draw_line(self):
        for trip in range(0, 10):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
            self.pendown()
            self.fd(20)