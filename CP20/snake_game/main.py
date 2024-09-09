from turtle import Turtle,Screen
import time  #add  time module 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Bam Game")
screen.tracer(0) # Turn off animation effects

start_pos = [(-20,0),(0,0),(20,0)]

new_s=[]  # Empty array for structuring

for pos in start_pos:
    s_part = Turtle("square")
    s_part.color("green")
    s_part.penup() # No initial position drawing
    s_part.goto(pos)
    new_s.append(s_part) # Add object with coordinates to empty array

game_is_on = True
while game_is_on:
    screen.update() # Structured snake body updated in a connected state
    # for s in new_s:   
    #     s.forward(25)
    time.sleep(0.2)

    # The order in which the head, torso, and tail move when an object rotates.
    for s_movement_index in range(len(new_s)-1, 0 ,-1):
        mod_x = new_s[s_movement_index-1].xcor()
        mod_y = new_s[s_movement_index-1].ycor()
        new_s[s_movement_index].goto(mod_x,mod_y)
    new_s[0].forward(20)
    new_s[0].right(90)

screen.exitonclick()