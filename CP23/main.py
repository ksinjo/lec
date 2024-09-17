import time 
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

stage1 = 10
screen = Screen()
screen.title("박스 피해서 전진하기")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player(90)
scoreboard = Scoreboard()


car_manger = CarManager()
    

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.create_car()
    car_manger.move_cars()
#Detect Collision with car 
    for car in car_manger.all_cars:
        if car.distance(player) < 20:
            game_is_on = False 
            scoreboard.game_over()
            
            

#Detect Success finishLine 
    if player.finish():
        player.goto_start()
        car_manger.level_up()
        scoreboard.increase_level() # 스코어보드 난이도 갱신 함수 추가 


screen.exitonclick()