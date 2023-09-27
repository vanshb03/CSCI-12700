#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/20/2023
#A program that uses command strings to control turtle drawing

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'B':
        tess.backward(50)
    elif ch == 'S':
        tess.stamp()
    elif ch == 'l':
        tess.left(45)
    elif ch == 'r':
        tess.right(45)
    elif ch == 'p':
        tess.color("purple")
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", ch) #typo, was c before

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked




