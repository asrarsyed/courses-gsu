#   CSC 1301 – Section: 002
#   Python Homework #04
#   Due 11/07/2022 11.59 pm

'''
  Purpose:
    Create a image using turtle in python
  Pre-conditions (input): 
    None
  Post-conditions (output): 
    Output a image of a house in turtle window
'''
import turtle
from turtle import *
import math
import random

#   Making a Screen
screen = turtle.Screen()
screen.title("Image Drawing - The Sad Flowers")
screen.bgcolor("lightskyblue")
screen.setup(width=.85,height=.85)

turtle.hideturtle() # Hiding the Turtle for the entire code that uses Turtle
turtle.tracer(0,0) # Instant image

#   Function for Shapes
def draw_shapes(shape,width,height,X,Y,fill_color,pen_color,pen_size,pen_speed):
    if shape == "square":
        turtle.pen(fillcolor=fill_color, pencolor=pen_color, pensize=pen_size, speed=pen_speed)
        turtle.penup()
        turtle.goto(X,Y)
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
        turtle.pen(fillcolor=fill_color, pencolor=pen_color, pensize=pen_size, speed=pen_speed)
        turtle.penup()
        turtle.goto(X,Y)
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
        turtle.pen(fillcolor=fill_color, pencolor=pen_color, pensize=pen_size, speed=pen_speed)
        turtle.penup()
        turtle.goto(X,Y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(300) # draw base
        turtle.left(135)
        turtle.forward(300/math.sqrt(2))
        turtle.left(90)
        turtle.forward(300/math.sqrt(2))
        turtle.end_fill()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    if shape == "circle":
        turtle.pen(fillcolor=fill_color, pencolor=pen_color, pensize=pen_size, speed=pen_speed)
        turtle.penup()
        turtle.goto(X,Y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(width)
        turtle.penup()
        turtle.home()
        turtle.pendown()

#   Drawing the Grass
draw_shapes("rectangle",1300,500,-650,-150,"forestgreen","forestgreen",0,0)

#   Drawing the Sun
draw_shapes("circle",45,45,-400,200,"yellow","darkorange",0,0)




turtle.exitonclick()
