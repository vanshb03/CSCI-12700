#Date: 08/31/2023
#This program will be making the a Five-Pointed Star using the Turtle module.

import turtle
wn = turtle.Screen()

thomasH = turtle.Turtle()

for i in range(5):
    thomasH.forward(100)
    thomasH.left(144)

turtle.Screen().exitonclick()
