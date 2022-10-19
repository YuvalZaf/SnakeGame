from turtle import Turtle
import random


class Food(Turtle):  # constructor
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_food()

    def new_food(self):  # place a new food pill on the board
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
