from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')
with open("snake_high_score.txt", mode = "r") as file:
    # can use assert to make sure it only contains a number
    RECORD_HIGH_SCORE = int(file.read())

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = RECORD_HIGH_SCORE
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", 
                   False, align = ALIGNMENT, font = FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.record_new_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER!", False, align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def record_new_high_score(self):
        if self.high_score > RECORD_HIGH_SCORE:
            with open("snake_high_score.txt", mode = "w") as file:
                file.write(str(self.high_score))