import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")



game_is_on = True
rotation_count = 0
while game_is_on:
    time.sleep(0.1)
    rotation_count += 1
    screen.update()
    # can use randint(1, 6) to create new car as well
    if rotation_count % 6 == 0:
        num_cars = random.randint(0, 1)
        for _ in range(num_cars):
            car_manager.create_new_car()
    for car in car_manager.cars:
        car.car_move()
        # Detect collision with cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        if player.ycor() >= 295:
            scoreboard.next_level()
            player.player_reset()
            car_manager.speed_up_all_cars()
            


screen.exitonclick()