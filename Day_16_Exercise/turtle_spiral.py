from turtle import Turtle, color, forward, right, Screen
tommy = Turtle()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

my_screen = Screen()
my_screen.exitonclick()