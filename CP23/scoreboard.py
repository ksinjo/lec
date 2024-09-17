from turtle import Turtle
from player import Player
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1 
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        
        self.clear() # 이전 write 겹치므로 초기화 
        self.write(f"LEVEL:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1 
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)