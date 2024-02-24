from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_PADDLE_COORDINATES = (350, 0)
L_PADDLE_COORDINATES = (-350, 0)


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_COORDINATES)
l_paddle = Paddle(L_PADDLE_COORDINATES)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
ball_bounce = 0
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with the paddle

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball_bounce == 0 or ball.distance(l_paddle) < 50 and
            ball.xcor() < -320 and ball_bounce == 0):
        ball.bounce_x()
        ball_bounce = 1

    if ball.xcor() == 0:
        ball_bounce = 0

    # Detect R paddle misses:
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_pos()

    # Detect L paddle misses:
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_pos()

screen.exitonclick()
