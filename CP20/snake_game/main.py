# import pygame
# pygame.init()
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
        feedstuff.refresh()
        scoreboard.increase_score() # call Func
      

    if snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor()>290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()