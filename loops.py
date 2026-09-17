import turtle
from turtle import *
t=Turtle()
t.speed(0)
t.shape("turtle")
'''
def square(x,y):
    t.fd(x)
    t.lt(y)
    t.fd(x)
    t.lt(y)
    t.fd(x)
    t.lt(y)
    t.fd(x)
    t.lt(y)
for i in range(100):
    square(200,90)
    t.lt(5)'''
  
def doublesquares(iRange):
    length=5
    for i in range(iRange):
        square(length,90)
turtle.done()