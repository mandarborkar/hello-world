import turtle
import time
def drawsquare (x,y):
    myturtle.penup()
    myturtle.setpos (x,y)
    myturtle.pendown()
    myturtle.forward (100)
    myturtle.left (90)
    myturtle.forward (100)
    myturtle.left (90)
    myturtle.forward (100)
    myturtle.left (90)
    myturtle.forward (100)

myturtle = turtle.Turtle()
drawsquare(-300,0)
drawsquare(-200,0)
drawsquare(0,100)
drawsquare(100,-100)
# upload latest
'''
myturtle.speed(20)
for i in range(180):
    myturtle.forward(100)
    myturtle.right(30)
    myturtle.forward(20)
    myturtle.left(60)
    myturtle.forward(50)
    myturtle.right(30)

    myturtle.penup()
    myturtle.setposition(0, 0)
    myturtle.pendown()

    myturtle.right(2)
'''
turtle.done()