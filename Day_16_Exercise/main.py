import another_module
print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()
# which is the same as
from turtle import *
tommy = Turtle()
print(tommy)
tommy.shape("turtle")
tommy.color("coral")

# get the turtle back to the center
home()
# set the width of the line
# width(5)
forward(100)
left(120)
forward(100)
left(120)
forward(100)



my_screen = Screen()
# this will print the width of the screen, which is an attribute of the Screen class object
print(my_screen.canvheight)
my_screen.exitonclick()
