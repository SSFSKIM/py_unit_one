import turtle

#simple house
def draw_house(size, square, triangle):
    turtle.begin_fill()
    for a in range(4):
        turtle.fillcolor(square)
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.begin_fill()
    for a in range(3):
        turtle.fillcolor(triangle)
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(2*size)
    turtle.pendown()

for a in ((30, 'red', 'blue'), (50, 'violet', 'navy'), (70, 'green', 'cyan'), (20, 'yellow', 'orange')):
    draw_house(a[0], a[1], a[2])
