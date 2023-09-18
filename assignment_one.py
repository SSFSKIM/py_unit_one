#Steve
#09.16

import turtle
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        turtle.Turtle(c)
        turtle.forward(steps)
        turtle.right(30)
turtle.exitonclick()