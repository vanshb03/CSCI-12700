#Date: 09/11/2023
#This program asks the user for the hexcode of a color and then displays a turtle that color using the Turtle module.

import turtle

word = input("Enter a hex string: ")

turt = turtle.Turtle()
turt.shape("turtle")
turt.color(word)


turtle.Screen().exitonclick()
