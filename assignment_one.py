#Steve
#09.16

import turtle
import math
turtle.speed(10)
def istar():
    turtle.begin_fill()
    for a in range(6):
        turtle.fillcolor('navy')
        turtle.forward(30)
        turtle.right(60)
        turtle.forward(30)
        turtle.left(120)
    turtle.end_fill()

def diamond():
    turtle.begin_fill()
    turtle.fillcolor('light blue')
    for a in range(2):
        turtle.forward(30)
        turtle.left(60)
        turtle.forward(30)
        turtle.left(120)
    turtle.end_fill()
def diamonds():
    turtle.left(180)
    for a in range(6):
        diamond()
        turtle.penup()
        turtle.left(150)
        turtle.forward(30*math.sqrt(3))
        turtle.pendown()
        turtle.right(90)
def triangles():
    turtle.left(60)
    turtle.forward(30)
    turtle.left(30)
    for a in range(6):
        turtle.begin_fill()
        for a in range(3):
            turtle.forward(30*math.sqrt(3))
            turtle.left(120)
            turtle.fillcolor('turquoise')
        turtle.end_fill()
        turtle.penup()
        turtle.forward(15 * math.sqrt(3))
        turtle.left(90)
        turtle.forward(75)
        turtle.pendown()
        turtle.right(30)
def Mosaic():
    istar()
    diamonds()
    triangles()
    turtle.penup()
    turtle.forward(-15*math.sqrt(3))
    turtle.left(90)
    turtle.forward(15)
    turtle.pendown()
turtle.speed(200)
def move_60():
    turtle.penup()
    turtle.forward(225)
    turtle.left(90)
    turtle.forward(45*math.sqrt(3))
    turtle.left(30)
    turtle.pendown()

def move_180():
    turtle.penup()
    turtle.forward(135)
    turtle.left(90)
    turtle.forward(45 * math.sqrt(3))
    turtle.right(90)
    turtle.pendown()
turtle.speed(20000)
def Moroccan():
    n=1
    for a in range(1000):
        Mosaic()
        move_60()
        for b in range(n):
            Mosaic()
            move_180()
        n+=1
Moroccan()


turtle.exitonclick()