import turtle
from turtle import *
t=Turtle()
t.shape('turtle')

"""t.fd(200)
def message(input):
    print(input)
message("Hello Class")
t.speed(10)
def square(x):
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(x)
square(200)"""

def equal(x):
    t.fd(x)
    t.rt(120)
    t.fd(x)
    t.rt(120)
    t.fd(x)
equal(200)
def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()

turtle.done()
