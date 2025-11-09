from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward(step = 10):
    tim.fd(step)

def move_backward(step = 10):
    tim.bk(step)

def move_counter_clockwise(angle = 10):
    tim.lt(angle)

def move_clockwise(angle = 10):
    tim.rt(angle)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_counter_clockwise)
screen.onkey(key = "d", fun = move_clockwise)
screen.onkey(key = "c", fun = clear_drawing)

screen.exitonclick()