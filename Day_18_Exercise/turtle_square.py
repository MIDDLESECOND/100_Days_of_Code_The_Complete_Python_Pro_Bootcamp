from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

rotate_corner = 0

while rotate_corner < 360:
    timmy.forward(100)
    timmy.right(90)
    rotate_corner += 90

screen = Screen()
screen.exitonclick()