from turtle import Turtle


ALIGNMENT = "center"
FONT= ("courier",20,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("azure")
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial",24,"normal"))


    def increase_score(self):
        self.score += 10
        print("Yum yum yum!! Get 10 point ")
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT, font=FONT)
        print("뱀 망사 사망")

    def game_over2(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT, font=FONT)
        print("배고픈 당신은 자신의 꼬리를 먹고 죽었졍! 너 다이! ")