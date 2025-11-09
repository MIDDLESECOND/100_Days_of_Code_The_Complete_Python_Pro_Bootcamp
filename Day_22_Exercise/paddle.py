from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

class Paddle(Turtle):
    
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        # self.hideturtle()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        # the stretch is multiplier......
        # self.shapesize(stretch_len = PADDLE_HEIGHT / 2, stretch_wid = PADDLE_WIDTH / 2)
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.goto(starting_position[0], starting_position[1])
        # self.showturtle()
        # hiding and showing could work, but the screen tracer method is better

    def up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.xcor(), new_y_position)
    
    def down(self):
        new_y_position = self.ycor() - 20
        self.goto(self.xcor(), new_y_position)