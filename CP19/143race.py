from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="돈 내고 돈 먹귀", prompt="어떤 색 거북이 이길까요? 컬러색을 입력: ")
colors=["red","orange","yellow","green","blue","purple"]
y_position= [-70, -40, -10, 20, 50, 80]

for item  in range(len(colors)):
    t1 = Turtle(shape="turtle")
    t1.color(colors[item])
    t1.penup()
    t1.goto(x=-230,y=y_position[item])

print(user_bet)

screen.exitonclick()