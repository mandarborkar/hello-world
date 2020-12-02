import turtle
import time
# upload latest
def drawsunshine (mturtle, x,y,size,angle):
    mturtle.penup()
    mturtle.setpos(x, y)
    mturtle.pendown()
    mturtle.pencolor("yellow")
    repeatangle=360/angle
    for i in range(int(repeatangle)):
        mturtle.setpos(x, y + size)
        mturtle.forward(1.5 * size)
        mturtle.right(angle)
        mturtle.penup()
        mturtle.setpos(x, y)
        mturtle.pendown()

def drawsun (mturtle, x,y,size):
    mturtle.penup()
    mturtle.setpos(x, y)
    mturtle.pendown()
    mturtle.fillcolor("yellow")
    mturtle.begin_fill()
    mturtle.circle(size)
    mturtle.end_fill()
    drawsunshine(mturtle,150,150,50,10)

def drawperson (mturtle, x, y, personsize,color,handangle,legangle):
    #body
    mturtle.pencolor(color)
    mturtle.penup()
    mturtle.setpos(x,y)
    mturtle.pendown()
    mturtle.right(0)
    mturtle.forward(personsize)
    #head
    mturtle.penup()
    mturtle.setpos(x+personsize+2.5,y-5)
    mturtle.pendown()
    mturtle.circle(5)
    #hands
    mturtle.penup()
    mturtle.setpos(x+personsize*.75, y)
    mturtle.pendown()
    mturtle.right (handangle)
    mturtle.forward (personsize/4)
    mturtle.backward(personsize/2)

    #leg 1
    mturtle.penup()
    mturtle.home()
    mturtle.setpos(x,y)
    mturtle.pendown()
    mturtle.right(legangle)
    mturtle.back(personsize / 2)

    #leg 2
    mturtle.penup()
    mturtle.home()
    mturtle.setpos(x,y)
    mturtle.pendown()
    mturtle.right(-1*legangle)
    mturtle.back(personsize / 2)

#main function
wn = turtle.Screen()
wn.bgcolor("grey")
drawsomethingturtle = turtle.Turtle()

#draw sun
turtle.tracer(20)
drawsun(drawsomethingturtle,150,150,50)

#draw person
turtle.tracer(50)
for i in range (-200,200,50):
    drawsomethingturtle.penup()
    drawsomethingturtle.home()
    drawperson(drawsomethingturtle, i, 0, 50, "blue", 45, 20)
    time.sleep(2)

    turtle.clear ()
    drawsomethingturtle.penup()
    drawsomethingturtle.home()
    drawperson(drawsomethingturtle,i,0,50,"grey",45,20)

    drawsomethingturtle.penup()
    drawsomethingturtle.home()
    drawperson(drawsomethingturtle,i+25,0,50,"blue",-45,0)
    time.sleep(2)

    turtle.clear ()
    drawsomethingturtle.penup()
    drawsomethingturtle.home()
    drawperson(drawsomethingturtle,i+25,0,50,"grey",-45,0)
    #drawsomethingturtle.circle(10)
#finish
turtle.exitonclick ()