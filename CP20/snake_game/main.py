# import pygame
# pygame.init()

# 추가적으로 만들어 보고 싶은 것
# pygame 배경 바꾸기 
# 뱀 길이에 따라 등급으로 나눠 종료 시 출력하기 

from turtle import Screen
from snake import Snake #/ import Snake 
from feedstuff import Feedstuff
import time  #add  time module 
from scoreboard import Scoreboard

# pygame.display.set_caption("뱀 이다")

# back = pygame.image.load("D:/python_project/lec/CP20/snake_game/back.png")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# screen_width= 600
# screen_height= 600
# screen = pygame.display.set_mode((screen_width,screen_height))
# screen.bgpic("forest.png")
screen.title("배미다 뱀이다냥!")
screen.tracer(0) # Turn off animation effects

scoreboard = Scoreboard()
snake = Snake() # / Create Instance 
feedstuff = Feedstuff()

# Empty array for structuring

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    # screen.blit(back,(0,0))
    # pygame.display.update()
    screen.update() # Structured snake body updated in a connected state
    time.sleep(0.1)

    snake.move()  #/ call the snake move method
    if snake.head.distance(feedstuff) < 15:
        print(f"{int(snake.head.xcor())},{int(snake.head.ycor())} 뱀 사료를 겟토! ")
        feedstuff.refresh()
        # print(f"next food x pos : {feedstuff.xcor}, next food y 좌표: {feedstuff.ycor}")
        snake.extend()
        scoreboard.increase_score() # call Func
      
    # check Collision wall.
    if snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor()>290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # check Collision head meet tail
    for part in snake.new_s[1:]:
        # if part == snake.head:
        #     pass
        if snake.head.distance(part) <10:
            game_is_on = False
            scoreboard.game_over2()

screen.exitonclick()