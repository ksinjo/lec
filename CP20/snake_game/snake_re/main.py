from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

start_pos= [(-20,0),(0,0),(20,0)]
new_pos = []

game_is_on = True

for pos in start_pos:
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(pos)
    new_pos.append(snake_segment)



while game_is_on:
    for snake in new_pos:
        snake.forward(20)


screen.exitonclick()