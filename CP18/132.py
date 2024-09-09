import turtle as t 
import random

# tt = t.Turtle()
# t1 = t.Turtle()

# t1.shape("square")
# tt.shape("turtle")
# tt.color("red")

# for _ in range(5):
#     tt.forward(100)
#     tt.right(360/5)


# for _ in range(8):
#     t1.forward(100)
#     t1.right(360/8)


t1 = t.Turtle()
t1.shape("turtle")
t1
colors= ["cornflower blue","green yellow","chartreuse","gold","coral","IndianRed","DeepSkyBlue","wheat","aquamarine","dark salmon","light sky blue"]

def draw_shape(num_sides):
   
    for _ in range(num_sides):
        angle = 360 / num_sides
        t1.forward(100)
        t1.right(angle)

for item in range(3,15):
    t1.color(random.choice(colors)) # 컬러 랜덤 선택 
    draw_shape(item)

