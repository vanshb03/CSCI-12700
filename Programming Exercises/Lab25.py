#Date: 09/20/2023
#This program implements a turtle graphics interpreter that takes a user-input command string, where each character corresponds to a specific action (e.g., moving forward, turning left or right, lifting or lowering the pen, stamping, changing color), and visualizes the corresponding turtle graphics on a window using the Turtle module.

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
    elif ch == 'B':         #move backward
        tess.backward(50)
    elif ch == 'S':         #Stamp
        tess.stamp()
    elif ch == 'l':         #Turn left by 45 degrees
        tess.left(45)
    elif ch == 'r':         #Turn right by 45 degrees
        tess.right(45)
    elif ch == 'p':         #Add color :)
        tess.color("purple")
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", ch) #typo, was c before

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked




