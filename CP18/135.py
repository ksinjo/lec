import turtle as c
import random 

c.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

cir = c.Turtle()
cir.speed("fastest")
def draw_spigrpaph(gap):
    for _ in range(int(360/gap)):
        cir.color(random_color())
        cir.circle(180)
        current_heading = cir.heading()
        cir.setheading(current_heading + gap)
draw_spigrpaph(3)



screen = c.Screen()
screen.exitonclick()