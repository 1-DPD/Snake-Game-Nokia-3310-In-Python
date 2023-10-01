from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_food_location()

    def refresh_food_location(self):
        x_random_position = random.randint(-230, 230)
        y_random_position = random.randint(-230, 230)
        self.goto(x_random_position, y_random_position)
