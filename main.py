from turtle import Turtle,Screen
from scoreboard import Scoreboard
import turtle
from paddles import Paddles
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Jong")
screen.tracer(0)

r_paddle = Paddles((350,0))
l_paddle = Paddles((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# Moves the paddles
screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collsion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collsion with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < - 380:
        scoreboard.r_point()
        ball.reset_position()






screen.exitonclick()
