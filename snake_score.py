from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(210, 210)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align="right", font=("Ariel", 20, "normal"))

    def increasing_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Ariel", 20, "normal"))

