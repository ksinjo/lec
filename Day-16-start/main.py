# import another_module
# print(another_module.another_variable)

# import turtle 
from turtle import Turtle, Screen #Screen 
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(25)
timmy.right(90)
timmy.forward(100)
my_screen = Screen() # add Screen class
print(my_screen.canvheight) 

my_screen.exitonclick()
