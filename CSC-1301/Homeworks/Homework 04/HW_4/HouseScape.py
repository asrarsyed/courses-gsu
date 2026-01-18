#   CSC 1301 – Section: 002
#   Python Homework #04
#   Due 11/07/2022 11.59 pm

"""
  Purpose:
    Create a image using turtle in python
  Pre-conditions (input): 
    None
  Post-conditions (output): 
    Output a image of a house in turtle window
"""
import turtle
from turtle import *
import tkinter as TK
import math
import random

#   Making a Screen
screen = turtle.Screen()
screen.title("Image Drawing - The Sad Flowers")
screen.bgcolor("#FED59F")
screen.setup(width=1180, height=780)

turtle.hideturtle()  # Hiding the Turtle for the entire code that uses Turtle

turtle.tracer(0, 0)  # Instant image

#   Function for Shapes
def draw_shapes(shape, width, height, X, Y, fill_color, pen_color, pen_size, pen_speed):
    if shape == "square":
        turtle.pen(
            fillcolor=fill_color, pencolor=pen_color, pensize=pen_size, speed=pen_speed
        )
        turtle.penup()
        turtle.goto(X, Y)
        turtle.pendown()

        turtle.begin_fill()
        for i in range(2):
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    if shape == "rectangle":
        turtle.pen(
            fillcolor=fill_color, pencolor=pen_color, pensize=pen_size, speed=pen_speed
        )
        turtle.penup()
        turtle.goto(X, Y)
        turtle.pendown()

        turtle.begin_fill()
        for i in range(2):
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    if shape == "triangle":
        turtle.pen(
            fillcolor=fill_color, pencolor=pen_color, pensize=pen_size, speed=pen_speed
        )
        turtle.penup()
        turtle.goto(X, Y)
        turtle.pendown()

        turtle.begin_fill()
        turtle.forward(300)  # draw base
        turtle.left(135)
        turtle.forward(300 / math.sqrt(2))
        turtle.left(90)
        turtle.forward(300 / math.sqrt(2))
        turtle.end_fill()
        turtle.penup()
        turtle.home()
        turtle.pendown()


#   Drawing the Grass
draw_shapes("rectangle", 1200, 400, -600, -125, "#70c048", "forestgreen", 0, 0)

#   Drawing the Sun
sun = turtle.Turtle()
sun.hideturtle()
sun.pen(fillcolor="yellow", pencolor="red", pensize=1, speed=0)

sun.penup()
sun.goto(-550, 250)
sun.pendown()
sun.begin_fill()
sun.circle(100)
sun.end_fill()

#   Creating the House - Part 1
draw_shapes("square", 250, 250, 100, 100, "#c9b7a4", "black", 3, 0)

#   Creating the Roof - Part 2
draw_shapes("triangle", 1, 1, 75, 100, "#536d98", "black", 3, 0)

#   Creating the Chimney - Part 3
draw_shapes("rectangle", 40, 100, 275, 225, "darkgoldenrod", "black", 3, 0)

#   Creating the Door + Doorknob - Part 4
draw_shapes("rectangle", 60, 100, 200, -50, "#985c53", "black", 3, 0)

turtle.penup()
turtle.goto(215, -115)
turtle.pendown()
turtle.fillcolor("maroon")
turtle.begin_fill()
turtle.circle(2)
turtle.end_fill()
turtle.penup()
turtle.home()
turtle.pendown()

#   Function to Make the Window Lines - Part 5
def window(X, Y):
    turtle.penup()
    turtle.goto(X, Y)
    turtle.pendown()

    turtle.penup()
    turtle.forward(30)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.backward(60)
    turtle.left(90)
    turtle.penup()
    turtle.home()
    turtle.pendown()


#   Creating the Pathway
draw_shapes("rectangle", 80, 400, 190, -150, "lightslategray", "black", 3, 0)

#   Creating the Road
draw_shapes("rectangle", 300, 400, -450, -125, "lightslategray", "black", 3, 0)

#   Creating the small Road things
draw_shapes("rectangle", 15, 30, -300, -125, "white", "black", 3, 0)  #   Road 1

draw_shapes("rectangle", 15, 30, -300, -170, "white", "black", 3, 0)  #   Road 2

draw_shapes("rectangle", 15, 30, -300, -215, "white", "black", 3, 0)  #   Road 3

draw_shapes("rectangle", 15, 30, -300, -260, "white", "black", 3, 0)  #   Road 4

draw_shapes("rectangle", 15, 30, -300, -305, "white", "black", 3, 0)  #   Road 5

draw_shapes("rectangle", 15, 30, -300, -350, "white", "black", 3, 0)  #   Road 6

#   Creating some Windows
draw_shapes("square", 60, 60, 195, 185, "lightcyan", "black", 3, 0)  #   Window 1
window(195, 185)

draw_shapes("square", 60, 60, 125, 50, "lightcyan", "black", 3, 0)  #   Window 2
window(125, 50)

draw_shapes("square", 60, 60, 265, 50, "lightcyan", "black", 3, 0)  #   Window 3
window(265, 50)

#   Function for Trees
def trees(X, Y):
    #   Tree Trunk
    draw_shapes("rectangle", 30, 120, X, Y, "saddlebrown", "saddlebrown", 0, 0)
    #   Tree Leaves
    turtle.penup()
    turtle.goto(X + 15, Y - 3)
    turtle.pendown()

    turtle.color("darkseagreen")
    turtle.begin_fill()
    turtle.circle(75)
    turtle.end_fill()
    turtle.penup()
    turtle.home()


#   Creating some Trees
trees(450, -35)  #   Tree 1

trees(-35, -35)  #   Tree 2


#   Function for Clouds
cloud = turtle.Turtle()
cloud.hideturtle()


def clouds(size):
    cloud.pen(fillcolor="white", pencolor="white", pensize=2, speed=0)

    cloud.begin_fill()
    cloud.circle(size, 180)
    cloud.right(100)
    cloud.circle(size + 10, 150)
    cloud.right(100)
    cloud.circle(size + 20, 180)
    cloud.right(100)
    cloud.circle(size, 200)
    cloud.right(70)
    cloud.circle(size + 50, 50)
    cloud.right(70)
    cloud.circle(size, 120)
    cloud.end_fill()


#   Creating some Clouds
cloud.penup()
cloud.goto(-270, 200)  #   Cloud 1
cloud.pendown()
clouds(25)

cloud.penup()
cloud.right(90)
cloud.goto(470, 235)  #   Cloud 2
cloud.pendown()
clouds(20)

cloud.penup()
cloud.right(80)
cloud.goto(100, 275)  #   Cloud 3
cloud.pendown()
clouds(35)

#   Function for Flowers
color_list = (
    "red",
    "green",
    "pink",
    "blue",
    "lightblue",
    "limegreen",
    "grey",
    "tan",
    "thistle",
    "tomato",
    "mediumvioletred",
)


def flowers(X, Y):
    turtle.penup()
    turtle.goto(X, Y)
    turtle.pendown()
    #   Main Flower
    turtle.pen(
        fillcolor=random.choice(color_list), pencolor="black", pensize=3, speed=0
    )
    turtle.begin_fill()
    for i in range(5):
        turtle.circle(7, 180)
        turtle.right(108)
    turtle.end_fill()
    turtle.goto((X - 9), (Y + 7))
    turtle.color("yellow")
    turtle.dot(10)
    turtle.hideturtle()

    #   Flower Stem
    turtle.color("green")
    turtle.penup()
    turtle.goto((X - 9), (Y + 7))
    turtle.pendown()
    turtle.right(30)
    turtle.circle(-40, 80)
    turtle.penup()
    turtle.home()
    turtle.pendown()


#   Creating some Flowers
flowers(400, -85)  #   Flower 1

flowers(50, -85)  #   Flower 2

flowers(400, -170)  #   Flower 1

flowers(50, -170)  #   Flower 2

flowers(400, -255)  #   Flower 1

flowers(50, -255)  #   Flower 2

exitonclick()
