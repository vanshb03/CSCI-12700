#Date: 09/05/2023
#This program asks the user for 5 whole (integer) numbers. For each number using the turtle module, turn the turtle left the degrees entered and then the turtle should move forward 100.

import turtle

turt = turtle.Turtle()

for i in range(5):
    val = int(input("Enter a number:"))
    turt.left(val)
    turt.forward(100)

turtle.Screen().exitonclick()