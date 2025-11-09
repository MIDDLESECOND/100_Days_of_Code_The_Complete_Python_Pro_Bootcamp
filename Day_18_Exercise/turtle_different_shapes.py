from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")

colors = ['cornflower blue', 'blue', 'dark green', 'cyan', 'yellow', 'maroon', 'dark orange', 'indian red', 'magenta', 'medium slate blue']

for i in range(3, 9):
    n_degree = 360 / i
    timmy.color(choice(colors))
    degree_turned = 0
    while degree_turned <= 360:
        timmy.forward(100)
        timmy.right(n_degree)
        degree_turned += n_degree

screen = Screen()
screen.exitonclick()