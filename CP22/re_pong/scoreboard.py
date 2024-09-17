from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle
        self.l_score = 0
        self.r_score = 0
        # self.title = "Blue vs Yellow"
     
        self.update_score()
        
    def update_score(self):
        self.clear()

        self.goto(0,0)
        self.write("파랑 vs 노랭" ,align="center", font=("Courier",20,"normal"))
      
        self.color("pink")
        self.hideturtle  
        self.goto(-100,200)
   
        self.write(f"멍멍: {self.l_score}", align="center", font=("Courier",30,"normal"))
        self.hideturtle  

        self.goto(100,200)
        self.write(f"냥냥: {self.r_score}", align="center", font=("Courier",30,"normal"))


    def l_get_point(self):
        self.l_score += 1
        self.update_score()

    def r_get_point(self):
        self.r_score += 1
        self.update_score()
    