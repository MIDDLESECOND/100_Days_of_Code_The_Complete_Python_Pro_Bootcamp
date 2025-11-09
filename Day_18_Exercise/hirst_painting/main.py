# import colorgram

# # Extract colors from the graph
# colors = colorgram.extract('hirst_painting_example.jpg', 30)

# rgb_colors = []

# for color in colors:
#     # print(color)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [(235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), 
               (196, 77, 19), (217, 133, 177), (193, 164, 15), (34, 106, 166), (11, 21, 62),
                (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 32, 127), 
                (233, 165, 197), (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), 
                (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232), (229, 73, 45), (169, 180, 229)]

# now for the painting
import turtle as t
from random import choice, randint

# set the colormode to 255 for RGB color
t.colormode(255)

timmy = t.Turtle()
timmy.shape("arrow")
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.teleport(-225, -225)

starting_position = timmy.position()
x_position = starting_position[0]
y_position = starting_position[1]

for row in range(10):
    for column in range(10):
        rgb_color = choice(color_list)
        timmy.dot(20, rgb_color)
        timmy.fd(50)
    timmy.teleport(x_position, (int(row) + 1) * 50 + y_position)

screen = t.Screen()
screen.exitonclick()