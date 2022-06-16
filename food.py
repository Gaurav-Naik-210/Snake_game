from turtle import Turtle
import random

colors = ["green", "blue", "purple", "pink", "yellow"]


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape("circle")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


