#Date: 09/07/2023
#This program will implements the pseudocode that makes a spiraling square shape going outwards using the Turtle module.

import turtle

thomasH = turtle.Turtle()

for x in range(5,305,5):
    thomasH.forward(x)
    thomasH.left(91)

turtle.Screen().exitonclick()
