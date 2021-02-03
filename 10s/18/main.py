import colorgram
import random
import turtle as t

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

# instantiate turtle and screen
tim = t.Turtle()
tim.shape('turtle')
tim.speed('fastest')
t.colormode(255)
tim.pu()

# starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# make the dots
def make_dots():
    for _ in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)

# go to next row
def next_row():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

for _ in range(3):
    make_dots()
    next_row()
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
