from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open ('high_score.txt') as self.file:
            self.high_score = int(self.file.read())
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(x=0, y=270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #    self.goto(x=0,y=0)
    #    self.write("GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode="w") as self.file:
                self.file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()
