from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.goto(0,0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        

    # def random_color(self):
        
    #     r = random.randint(0,255)
    #     g = random.randint(0,255)
    #     b = random.randint(0,255)
    #     self.rgb = (r,b,g)
     

    # def update_color(self):
    #     self.clear()
    #     self.random_color()
    #     self.color(self.rgb)
      
     


    def move(self):
        mov_x = self.xcor() + self.x_move
        mov_y = self.ycor() + self.y_move 
        self.goto(mov_x,mov_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        
        