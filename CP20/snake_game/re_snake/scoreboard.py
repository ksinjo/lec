from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("azure")
        self.write(f"Score :{self.score}",align="center",font = ("Courier",24,"normal"))
        self.hideturtle()
        
   

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_score()

    def update_score(self):
           self.write(f"Score :{self.score}",align="center",font= ("Courier",24,"normal"))



    def game_over(self):
           self.goto(0,0)
           self.write(f"GAME OVER ",align="center",font= ("Courier",24,"normal"))












# from turtle import Turtle
# FONT = ("Courier",24,"normal")

# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0 
#         self.penup()
#         self.color("azure")
#         self.goto(0,260)
#         self.hideturtle()
        
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.write(f"Score: {self.score}", align="center", font =FONT)

#     def increase_scoreboard(self):        
#         self.score += 10
#         self.clear()
#         self.update_scoreboard()

#     def game_over(self):
#         self.goto(0,0)
#         self.write(f"Game over {self.score}", align="center", font =FONT)