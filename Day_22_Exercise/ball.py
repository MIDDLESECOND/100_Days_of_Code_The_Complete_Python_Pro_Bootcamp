from turtle import Turtle

# INITIAL_BALL_SPEED = 6

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        # self.speed("fastest")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.ball_speed = INITIAL_BALL_SPEED
        # self.speed(self.ball_speed)
        # shall be changing the sleep time instead of the ball speed

    def ball_move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_bounce(self):
        self.y_move = -1 * self.y_move

    def paddle_bounce(self):
        self.x_move = -1 * self.x_move
        self.move_speed = self.move_speed * 0.9

#     def ball_speed_boost(self):
#       if self.ball_speed < 10:
#            self.ball_speed += 1
#            self.speed(self.ball_speed)
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_bounce()
