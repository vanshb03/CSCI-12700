#Date: 09/13/2023
#This program draws a cornflower blue pentagon using the turtle module.

import turtle

turt = turtle.Turtle()
turt.shape("turtle")
turt.color("cornflowerblue")

for i in range(5):
    turt.forward(100)
    turt.stamp()
    turt.left(72)


turtle.Screen().exitonclick()
