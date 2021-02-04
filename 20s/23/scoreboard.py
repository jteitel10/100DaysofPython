from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-280, 250)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align = 'left', font = FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = 'center', font = FONT)
    def increase_score(self):
        self.level += 1
        self.update_score()
