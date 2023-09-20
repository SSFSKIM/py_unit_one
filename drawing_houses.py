import turtle

#simple house
def draw_house(size, square, triangle):
    turtle.begin_fill()
    for a in range(4):
        turtle.fillcolor(square)
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()
    turtle.goto(0,size)
    turtle.begin_fill()
    for a in range(3):
        turtle.fillcolor(triangle)
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

for a in (30, 50, 70, 20):
    draw_house(a,  'red', 'blue')
