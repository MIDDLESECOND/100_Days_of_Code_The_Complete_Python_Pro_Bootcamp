from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# screen.update()

'''
game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.fd(20)
        # screen.update()
        
'''
# this cannot solve the turning problem

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    for seg_num in range((len(segments) - 1), 0, -1):
        x_position = segments[seg_num - 1].xcor()
        y_position = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x_position, y_position)
    segments[0].fd(20)
    segments[0].left(90)






screen.exitonclick()