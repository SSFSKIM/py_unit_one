import turtle

#code for rotated squares
'''
for a in range(3):
    turtle.left(25)
    for a in range(4):
        turtle.forward(100)
        turtle.left(90)

turtle.exitonclick()
'''
#code for symmetric diamonds
'''
turtle.right(30)
for a in range(6):
    for a in range(2):
        turtle.forward(50)
        turtle.left(60)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(50)
        turtle.right(60)
        turtle.forward(50)
        turtle.right(120)
        turtle.forward(50)
        turtle.right(60)
        turtle.forward(50)
        turtle.right(120)
        turtle.forward(50)
        turtle.left(60)
        turtle.forward(50)
        turtle.left(180)
        '''
#it can also be done with rotating hexagon
'''
turtle.left(30)
for a in range(6):
    turtle.left(60)
    for a in range(6):
        turtle.forward(50)
        turtle.left(60)
        '''
#code for sprial
'''
for a in range(30):
    for b in range(2):
        turtle.forward(200-5*a)
        turtle.right(90)
'''
#code for matrix
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.left(90)
def right_stick():
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
def left_stick():
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
def one_big():
    right_stick()
    left_stick()
for a in range(2):
    for a in range(2):
        for a in range(2):
            one_big()
        right_stick()
    turtle.right(90)
    turtle.goto(0,300)

turtle.exitonclick()