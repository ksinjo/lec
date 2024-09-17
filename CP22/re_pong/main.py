from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
screen.title(" 핑퐁 게임")
screen.tracer(0)



r_paddle = Paddle((360,0),"yellowgreen")
l_paddle = Paddle((-360,0),"royalblue")
l_paddle.settiltangle(180)
ball = Ball()
# ball.colormode(255)
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 340 or  ball.distance(l_paddle) < 40 and ball.xcor() < -340 :
        ball.bounce_x()

    # r paddle misses
    if ball.xcor() > 380 :
        ball.reset()
        Scoreboard.l_get_point()
        # ball.update_color()

    if ball.xcor() < -380:
        ball.reset()
        Scoreboard.r_get_point()
        # ball.update_color()

# paddle = Turtle(shape="square")
# paddle.color("pink")
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)

# paddle.goto(350,0)
# screen.update()

# def go_up():
#     new_y= paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)

# def go_down():
#     new_y= paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

# screen.listen()
# screen.onkey(go_up,"Up")
# screen.onkey(go_down,"Down")

# game_is_on = True 
# while game_is_on:
#     screen.update()

screen.exitonclick()







# 스크린 객체생성
# 스크린 크기 지정
# 백그라운드 색 지정
# 타이틀 지정
# 스크린 클릭 시 종료
