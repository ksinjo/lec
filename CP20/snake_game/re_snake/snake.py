from turtle import Turtle
import random 
U=90
D=270
L=180
R=0



EASY_SPEED = 20

start_pos=[(0,0),(-20,0),(-40,0)]

class Snake():
    def __init__(self):
        self.body = []
        self.create()
        self.head = self.body[0]
        self.head.color("red")

    # def create(self):
    #     for seg in start_pos:
    #         new_seg = Turtle(shape="square")
    #         new_seg.penup()
    #         new_seg.color("green")
    #         new_seg.goto(seg)
    #         self.body.append(new_seg) # 틀린 부분 


    def create(self):
        for seg in start_pos:
             self.add_seg(seg)


    def add_seg(self,pos):
            new_seg = Turtle(shape="square")
            new_seg.penup()
            new_seg.color("green")
            new_seg.goto(pos)
            self.body.append(new_seg) # 틀린 부분 

    def extend(self):
         self.add_seg(self.body[-1].pos())

    def move(self):
            for move_index in range(len(self.body)-1,0,-1):
                mod_x = self.body[move_index-1].xcor()
                mod_y = self.body[move_index-1].ycor()
                self.body[move_index].goto(mod_x,mod_y)
            self.body[0].forward(EASY_SPEED)
# body=[]

    def up(self):
         if self.head.heading() != D:
            self.head.setheading(U)

    def down(self):
         if self.head.heading() != U:
            self.head.setheading(D)

    def left(self):
         if self.head.heading() != R:
            self.head.setheading(L)

    def right(self):
         if self.head.heading() != L:
            self.head.setheading(R)

