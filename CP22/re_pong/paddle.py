from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos,color):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.color(color)
       
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)


