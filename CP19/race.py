from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("pink")
bet = screen.textinput(title= "어떤 느림보가 이길까?", prompt= "컬러 입력: ")

colors=["gold","indigo","slateblue","crimson","palegreen","greenyellow"]
y_pos = [-180,-120,-60,60,120,180]

l = Turtle()
l.penup()
l.goto(280,-280)
l.pensize(3)
l.pendown()
l.left(90)
l.forward(580)

all_t = [] # 여러개의 터틀을 배열로 저장 빈공간 


for item in range(0,6):
    t = Turtle(shape="turtle")
    t.shapesize(2,2)
    t.color(colors[item])
    t.penup()
    t.goto(x=-280,y=y_pos[item])
    all_t.append(t) # 배열에 터틀을 추가 

if bet:
    is_race_on = True 

while is_race_on:
    for t in all_t:
        if t.xcor()> 240:
            is_race_on = False
            screen.textinput(title="우승거북이", prompt=f"{t.pencolor()} 등딱지가 이겼다냥!! " )
            winning_color = t.pencolor()
            if winning_color == bet:
                print(f"니가 이겼대! {winning_color} 딱딱한놈 위너")
            else:
                print(f"돈 날렸쓰 ! {winning_color} 딱딱한놈 이김. 도박쟁이 도박 그만! ")
        ran_distance = random.randint(0,60)
        t.forward(ran_distance)

print(bet)
screen.exitonclick()