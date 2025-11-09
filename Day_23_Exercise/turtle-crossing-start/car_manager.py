from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):

    def __init__(self, move_distance = STARTING_MOVE_DISTANCE):
        super().__init__()
        self.hideturtle()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len = 2, stretch_wid = 1)
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.showturtle()
        self.move_distance = move_distance

    def car_move(self):
        self.goto(self.xcor() - self.move_distance, self.ycor())

    def car_speed_up(self):
        self.move_distance = self.move_distance + MOVE_INCREMENT


class CarManager():
    
    def __init__(self):
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        new_car = Car(move_distance = self.current_speed)
        self.cars.append(new_car)

    def speed_up_all_cars(self):
        self.current_speed += MOVE_INCREMENT
        for car in self.cars:
            car.move_distance = self.current_speed

    
