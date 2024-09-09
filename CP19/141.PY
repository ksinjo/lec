from turtle import Turtle, Screen

t1 = Turtle ()
screen = Screen()
t1.color("green")
t1.pensize(8)
t1.shape("turtle")
t1.speed("fast")
def move_forward():
    t1.forward(10)

def move_backward():
    t1.backward(10)

def turn_left():
    new_heading = t1.heading() + 10 
    t1.setheading(new_heading)

def turn_right():
    new_heading = t1.heading() - 10 
    t1.setheading(new_heading)

def clear():
    t1.clear()
    t1.home()

def pen_up():
    t1.penup()

def pen_down():
    t1.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.onkey(pen_up,"o")
screen.onkey(pen_down,"]")
screen.exitonclick()

