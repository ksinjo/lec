from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("뱀 게임")
screen.tracer()


snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    
    # for segment in snake.body:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()



    # for segment in snake.body:
    #     if segment == snake.head:
    #         pass

    #     elif snake.head.distance(segment) <20:
    #         game_is_on = False
    #         scoreboard.game_over()




    # if snake.head.distance(food) < 15:
    #     food.refresh()
    #     scoreboard.increase_scoreboard()

    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
    #     game_is_on = False 
    #     scoreboard.game_over()
    

screen.exitonclick()

