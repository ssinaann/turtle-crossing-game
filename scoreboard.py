from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', font=FONT, align='left')

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over.', font=FONT, align='center')


