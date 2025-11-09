from turtle import Turtle, Screen
import random

is_race_on = False

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

tim = Turtle()
screen = Screen()
tim.clear()
tim.hideturtle()
turtle_width = 40
turtle_height = 40
screen_width = 500
screen_height = 400
screen.setup(width = screen_width, height = screen_height)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(f'{user_bet} turtle is your bet.')

x_axis_starting_point = -230
y_axis_starting_point = -100
y_axis_adjustment = 30

for i in range(len(color_list)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(color_list[i])
    new_turtle.goto(x_axis_starting_point, y_axis_starting_point + i * y_axis_adjustment)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on == True:
    for turtle in turtle_list:
        if turtle.xcor() > ((screen_width / 2) - (turtle_width / 2)):
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f'Congratulations! turtle {user_bet} won!')
            else:
                print(f'Unfortunate, turtle {winning_turtle} won.')
            is_race_on = False
        else: 
            step = random.randint(0, 10)
            turtle.fd(step)

screen.exitonclick()