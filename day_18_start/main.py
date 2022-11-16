import turtle
from turtle import Turtle, Screen
from random import choice, randint
tim = Turtle()
tim.shape("classic")
tim.color("black")

#create a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# draw a dashed line
# for i in range(5):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
#colors =["MediumSlateBlue", "Magenta", "DarkMagenta", "OrangeRed", "Black", "Bisque", "Salmon", "DarkOliveGreen"]


# side = 3
# side_length = 100
#
# for i in range(8):
#     tim.color(choice(colors))
#     for j in range(side):
#         tim.right(360/side)
#         tim.forward(side_length)
#     side += 1

# Angela's solution

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(choice(colors))
#     draw_shape(shape_side_n)

# draw a random walk
# turtle.colormode(255)
#
# def random_colour():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
#
# tim.pensize(10)
# tim.speed("fastest")
# for i in range(200):
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.setheading(choice(directions))

# make a spirograph
turtle.colormode(255)


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    numero = int(360 / size_of_gap)
    for i in range(numero):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)



screen = Screen()
screen.exitonclick()