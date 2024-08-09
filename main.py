import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

# Setting up key listeners:
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()
    # Detecting when the turtle player collides with a car and stop the game if this happens:
    for car in car_manager.all_cars:
        if car.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()
    # Detecting successful crossing:
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
