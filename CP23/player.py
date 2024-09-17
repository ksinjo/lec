from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self,deg):
        super().__init__()
        self.shape("turtle")
        self.color("crimson")
        self.penup()
        self.setheading(deg)
        self.goto_start()

    
    def move(self):
        self.forward(MOVE_DISTANCE)
        # self.y = self.ycor()

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor()  > FINISH_LINE_Y:
            return True
        else :
            return False 
