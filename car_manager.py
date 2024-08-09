from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Creating cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and moving to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen:


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        # To reduce the frequency of the cars:
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # Generates a random y coordinate along the length of the screen with 50px gap on top and bottom:
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
















