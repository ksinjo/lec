from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("pink")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)


# class Paddle(Turtle):
#     def __init__(self,pos):
#         super().__init__()
#         self.paddle = Turtle(shape="square")
#         self.paddle.color("pink")
#         self.paddle.shapesize(stretch_wid=5, stretch_len=1)
#         self.paddle.penup()
# # screen.tracer()
#         self.paddle.goto(pos)
#         self.screen.update()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
