#Date: 08/31/2023
#This program will be making an Octagon using the turtle module.

import turtle
wn = turtle.Screen()

thomasH = turtle.Turtle()

for i in range(8):
    thomasH.forward(100)
    thomasH.left(45)

turtle.Screen().exitonclick()
