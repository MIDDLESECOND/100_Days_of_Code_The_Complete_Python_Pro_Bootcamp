import turtle as t
from random import choice, randint

# set the colormode to 255 for RGB color
t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")

def random_color():
    color_index = randint(0, 255)
    return color_index

# set the thickness of pen
timmy.pensize(1)

# speed up timmy
timmy.speed("fastest")

for i in range(360):
    red_rgb = random_color()
    green_rgb = random_color()
    blue_rgb = random_color()
    timmy.pencolor((red_rgb, green_rgb, blue_rgb))
    timmy.circle(radius = 100)
    timmy.right(1)


screen = t.Screen()
screen.exitonclick()