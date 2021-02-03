from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clockwise():
    tim.right(10)

def clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.pu()
    tim.setposition(0,0)
    tim.setheading(0)
    tim.pd()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
