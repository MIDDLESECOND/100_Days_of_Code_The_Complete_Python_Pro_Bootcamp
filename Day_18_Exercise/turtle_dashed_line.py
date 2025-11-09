from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

def move_dash_line(steps = 50):
    for i in range(steps):
        timmy.forward(1)
        x_axis_position = timmy.position()[0]
        y_axis_position = timmy.position()[1]
        timmy.teleport(x = x_axis_position + 1, y = y_axis_position)

if __name__ == '__main__':
    move_dash_line()
    screen = Screen()
    screen.exitonclick()