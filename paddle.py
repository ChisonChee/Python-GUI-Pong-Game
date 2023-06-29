from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.ycor = 0
        self.setposition(position)

    def paddle_up(self):
        self.ycor += 20
        self.sety(self.ycor)

    def paddle_down(self):
        self.ycor -= 20
        self.sety(self.ycor)
