#Name: Vansh Bataviya
#Date: November 2023
#Defining Main function that will print Hello World.

# Modified by: Vansh

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,360,90)
  trey.right(a)