from turtle import Turtle
MOVE_DISTANCE = 20
start_pos = [(0,0),(-20,0),(20,0)]
U=90
D=270
L=180
R=0


class Snake():
    def __init__(self):
        self.new_s=[]  
        self.create_snake()
        self.head = self.new_s[0] #  헤드 속성을 추가 
        # self.head = self.s[0] # 키 방향전환 시 

    def create_snake(self):
        for pos in start_pos:
            s_part = Turtle("square")
            s_part.color("green")
            s_part.penup() # No initial position drawing
            s_part.goto(pos)
            self.new_s.append(s_part) # Add object with coordinates to empty array


    def move(self):
            for s_movement_index in range(len(self.new_s)-1, 0 ,-1):
                mod_x = self.new_s[s_movement_index-1].xcor()
                mod_y = self.new_s[s_movement_index-1].ycor()
                self.new_s[s_movement_index].goto(mod_x,mod_y)
            self.head.forward(MOVE_DISTANCE) 
            

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

         