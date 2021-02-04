import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# import objects
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

# listen for key strokes
screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    # create and move cars
    carmanager.create_cars()
    carmanager.move_cars()
    # detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    # detect when turtle reaches the end
    if player.reaches_finish():
        scoreboard.increase_score()
        player.go_to_start()
        carmanager.increase_speed()

screen.exitonclick()
