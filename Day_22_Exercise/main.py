from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on == True:
    # screen is updated after pad created in line: paddle = Paddle()
    # if ball.xcor() <= 260 and ball.ycor() <= 260:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect Collision with right_paddle
    # checking the ball ycor with the range of paddle y cor shall also solve the problem
    if (ball.distance(r_paddle) <= 50 and ball.xcor() > 320) or (ball.distance(l_paddle) <= 50 and ball.xcor() < -320):
        ball.paddle_bounce()
        # ball.ball_speed_boost()

    # Detect when paddle misses
    if ball.xcor() > 380:
        scoreboard.left_paddle_score_increase()
        ball.reset_position()
        time.sleep(0.5)

    if ball.xcor() < -380:
        scoreboard.right_paddle_score_increase()
        ball.reset_position()
        time.sleep(0.5)
        


screen.exitonclick()