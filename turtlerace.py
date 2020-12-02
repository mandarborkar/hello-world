import turtle
import random
import time
# upload latest
increments = 10

# start line is at x=-250
StartLinex = -250
# end line is at x=250
EndLinex = 250

def Drawline (x,y):
    Myline = turtle.Turtle()
    Myline.penup()
    Myline.setpos(x, y)
    Myline.pendown()
    Myline.right(90)
    Myline.forward(2*y)
    Myline.hideturtle()

def SetTurtleAtStart (Myturtle, x, y, color):
    Myturtle.shape("turtle")
    Myturtle.penup()
    Myturtle.color(color)
    Myturtle.setpos(x, y)
    #Myturtle.pendown()

def PlaceTurtle (myturtle,x,y,endx,increment):
    if x < endx :
        myturtle.setpos(x,y)
    x = x + random.randint(0, increment)
    return x

def ReadySetGo (myturtle, text):
    myturtle.write(text, align="Center", font=("Verdana", 30, "normal"))
    time.sleep(1)
    myturtle.clear()

window = turtle.Screen()
window.bgcolor("light green")

# Call Drawline Function
Drawline(StartLinex,270)
Drawline(EndLinex,270)

# Setting up the turtles at the start line

WhiteTurtle = turtle.Turtle()
SetTurtleAtStart(WhiteTurtle,StartLinex-20,200,"white")

RedTurtle = turtle.Turtle()
SetTurtleAtStart(RedTurtle,StartLinex-20,150,"red")

OrangeTurtle = turtle.Turtle()
SetTurtleAtStart(OrangeTurtle,StartLinex-20,100,"orange")

YellowTurtle = turtle.Turtle()
SetTurtleAtStart(YellowTurtle,StartLinex-20,50,"yellow")

GreenTurtle = turtle.Turtle()
SetTurtleAtStart(GreenTurtle,StartLinex-20,0,"green")

BlueTurtle = turtle.Turtle()
SetTurtleAtStart(BlueTurtle, StartLinex-20,-50,"blue")

PurpleTurtle = turtle.Turtle()
SetTurtleAtStart(PurpleTurtle,StartLinex-20,-100,"purple")

BlackTurtle = turtle.Turtle()
SetTurtleAtStart(BlackTurtle,StartLinex-20,-150,"black")

# Ready Set Go

GoTurtle = turtle.Turtle()
GoTurtle.penup()
GoTurtle.color("black")
GoTurtle.setpos(0, 0)
GoTurtle.pendown()
ReadySetGo(GoTurtle, "Ready...")
ReadySetGo(GoTurtle, "Set...")
ReadySetGo(GoTurtle, "Go!!!")
GoTurtle.penup()
GoTurtle.hideturtle()

# Lets race
WhiteTurtlex = StartLinex-20
RedTurtlex = StartLinex-20
OrangeTurtlex = StartLinex-20
YellowTurtlex = StartLinex-20
GreenTurtlex = StartLinex-20
BlueTurtlex = StartLinex-20
PurpleTurtlex = StartLinex-20
BlackTurtlex = StartLinex-20


while WhiteTurtlex < EndLinex+5 and RedTurtlex < EndLinex+5 and OrangeTurtlex < EndLinex+5 \
        and YellowTurtlex < EndLinex+5 and GreenTurtlex < EndLinex+5 \
        and BlueTurtlex < EndLinex+5 and PurpleTurtlex < EndLinex+5 \
        and BlackTurtlex < EndLinex+5  :

    WhiteTurtlex=PlaceTurtle(WhiteTurtle, WhiteTurtlex,200, EndLinex+5, increments)
    RedTurtlex=PlaceTurtle(RedTurtle, RedTurtlex,150, EndLinex+5, increments)
    OrangeTurtlex=PlaceTurtle(OrangeTurtle, OrangeTurtlex,100, EndLinex+5, increments)
    YellowTurtlex=PlaceTurtle(YellowTurtle, YellowTurtlex,50, EndLinex+5, increments)
    GreenTurtlex=PlaceTurtle(GreenTurtle, GreenTurtlex,0, EndLinex+5, increments)
    BlueTurtlex=PlaceTurtle(BlueTurtle, BlueTurtlex,-50, EndLinex+5, increments)
    PurpleTurtlex=PlaceTurtle(PurpleTurtle, PurpleTurtlex,-100, EndLinex+5, increments)
    BlackTurtlex=PlaceTurtle(BlackTurtle, BlackTurtlex,-150, EndLinex+5, increments)

window.exitonclick()

