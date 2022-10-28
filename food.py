from turtle import Turtle as Class_turtle
from snake import SCREEN_HEIGHT, SCREEN_WIDTH
import random


class Food(Class_turtle):
    def __init__(self):
        """Create a static turtle representing food"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-SCREEN_WIDTH * 0.45, SCREEN_WIDTH * 0.45)
        random_y = random.randint(-SCREEN_HEIGHT * 0.45, SCREEN_HEIGHT * 0.45)
        self.goto(x=random_x, y=random_y)
