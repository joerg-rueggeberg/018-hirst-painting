from random import choice, randint
from turtle import Turtle, Screen

colors = [
    (208, 149, 112), (229, 248, 77), (89, 247, 185), (83, 29, 14), (168, 8, 108), (20, 17, 91),
    (167, 79, 32), (89, 5, 63), (234, 36, 158), (81, 111, 239), (23, 97, 22), (32, 185, 84),
    (43, 12, 181), (24, 98, 179), (183, 183, 244), (229, 112, 175), (242, 65, 29), (51, 230, 64),
    (123, 159, 225), (186, 39, 129), (83, 16, 250), (66, 246, 251), (170, 15, 8), (55, 94, 7),
    (119, 169, 19), (44, 132, 47)]

turtle = Turtle()
turtle.speed(15)

screen = Screen()
screen.colormode(255)

turtle.pu()
turtle.setpos((-250, -250))

for line in range(10):
    for dot in range(10):
        if randint(1, 10) >= 3:
            turtle.dot(20, choice(colors))
            turtle.forward(50)
        else:
            turtle.forward(50)
    turtle.bk(500)
    turtle.seth(90)
    turtle.fd(50)
    turtle.seth(0)
turtle.hideturtle()

screen.exitonclick()
