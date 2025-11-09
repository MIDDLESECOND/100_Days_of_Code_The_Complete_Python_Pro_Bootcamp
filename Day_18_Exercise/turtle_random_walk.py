from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")

colors = ['cornflower blue', 'blue', 'dark green', 'cyan', 'yellow', 'maroon', 'dark orange', 'indian red', 'magenta', 'medium slate blue']
degree_to_turn = [0, 90, 180, 270]

# set the thickness of pen
timmy.pensize(5)

# speed up timmy
timmy.speed(0)

for i in range(50):
    timmy.color(choice(colors))
    timmy.forward(10)
    timmy.right(choice(degree_to_turn))

screen = Screen()
screen.exitonclick()