import turtle as t
from random import choice, randint

# set the colormode to 255 for RGB color
t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")

def random_color():
    color_index = randint(0, 255)
    return color_index

degree_to_turn = [0, 90, 180, 270]

# set the thickness of pen
timmy.pensize(5)

# speed up timmy
timmy.speed("fastest")

for i in range(200):
    red_rgb = random_color()
    green_rgb = random_color()
    blue_rgb = random_color()
    timmy.pencolor((red_rgb, green_rgb, blue_rgb))
    timmy.forward(10)
    timmy.setheading(choice(degree_to_turn))

screen = t.Screen()
screen.exitonclick()