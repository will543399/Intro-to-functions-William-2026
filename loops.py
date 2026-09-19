import turtle
from turtle import *
t=Turtle()
t.speed(0)
t.shape("turtle")

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
    t.lt(5)

  
def doublesquare(iRange):
    length=5
    for i in range(iRange):
        square(length,90)
        length=length*2
doublesquares(5)
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(5,90)
length=10
for i in range(60):
    square(length,90)
    length=length + 5
    t.rt(5)

length=10
def star(length):
    for i in range(5):
        t.fd(length)
        t.rt(144)
for i in range(60):
    star(length)
    length=length+5
    t.rt(5)


turtle.done()
# name=Inaya
#String are for characters
#Input asks the user a question and records the answer
#Input always outputs a string
# What we write in the input arguement is what the users sees
#bill = input("How much was the bill")
#Print("bill")
#if bill==10:
#   print("Match"):
#   else:
#   print("no match")

#integer
#amt=100

#Float
#amt2=99.99

#Boolean
#x=True
#y=False
turtle.done()
