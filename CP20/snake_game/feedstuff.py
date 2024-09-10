from turtle import Turtle
import random

class Feedstuff(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # r = random.randint(0,255)
        # g = random.randint(0,255)
        # b = random.randint(0,255)
        self.color("deeppink")
        self.speed("fastest")
        ran_x = random.randint(-280,280)
        ran_y = random.randint(-280,280)
        self.goto(ran_x,ran_y)
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-280,280)
        ran_y = random.randint(-280,280)
        self.goto(ran_x,ran_y)