import turtle as gom
import random

g = gom.Turtle()
gom.colormode(100)

def random_color():
    r = random.randint(0,100)
    g = random.randint(0,100)
    b = random.randint(0,100)
    random_color = (r,g,b)
    return random_color


directions=[0,90,180,270]
g.pensize(15)
g.shape("turtle")
g.speed("fast")

for _ in range(200):
    g.color(random_color())
    g.forward(45)
    g.setheading(random.choice(directions))
