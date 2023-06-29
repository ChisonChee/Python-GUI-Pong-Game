from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, MiddleLine
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PongPong")

screen.tracer(0)
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
scoreboard_l = Scoreboard((-100, 200))
scoreboard_r = Scoreboard((100, 200))
middle_line = MiddleLine()
middle_line.draw_line()


screen.onkeypress(paddle_l.paddle_up, "Up")
screen.onkeypress(paddle_l.paddle_down, "Down")
screen.onkeypress(paddle_r.paddle_up, "w".lower())
screen.onkeypress(paddle_r.paddle_down, "s".lower())
screen.listen()

play = True
while play:
    time.sleep(ball.frequency)
    screen.update()
    ball.ball_movement()
    scoreboard_l.display()
    scoreboard_r.display()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r.position()) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(paddle_l.position()) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.home()
        ball.frequency = 0.1
        ball.bounce_x()
        scoreboard_l.score += 1
        scoreboard_l.clear()

    if ball.xcor() < -350:
        ball.home()
        ball.frequency = 0.1
        ball.bounce_x()
        scoreboard_r.score += 1
        scoreboard_r.clear()

screen.exitonclick()
