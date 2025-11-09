from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.dn, "Down")
screen.onkey(snake.lt, "Left")
screen.onkey(snake.rt, "Right")


game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()