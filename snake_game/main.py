
from turtle import Screen, Turtle

#create 3 squares one next to each other
for cuadrado in range(3):
    new_cuadrado = Turtle(shape="square")
    new_cuadrado.color("white")
    new_cuadrado.pensize(20)
    x = cuadrado * (-20)
    new_cuadrado.goto(x, 0)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("La viborita")












screen.exitonclick()