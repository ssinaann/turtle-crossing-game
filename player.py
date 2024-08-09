from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Creating a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle north.


car = CarManager()
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        self.forward(10)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)








