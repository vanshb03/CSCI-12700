#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/12/2023
#This highlights what was covered in Lec_3

# More on Strings: Indexing & Substrings
s = "FridaysSaturdaysSundays"
# Accessing the character at index 7 (8th character) in the string.
days = s[7]
print(days)

# Slicing the string from index 7 to 15 (exclusive), extracting "Saturdays".
days = s[7:15]
print(days)

# Slicing the string from the beginning to the second-to-last character.
# This removes the last character "s".
days = s[:-1]
print(days)

# ⁡⁣⁢⁣Some arithmetic operators in Python:
#     Addition: sum = sum + 3
#     Subtraction: amt = amt - item
#     Multiplication: area = h * w
#     Division: ave = total / n
#     Floor or Integer Division:
#     weeks = totalDays // 7 15 // 7 = 2
#     Remainder or Modulus:
#     days = totalDays % 7 15 % 7 = 1
#     Exponentiation:
#     pop = 2**time⁡

# Challenge (Group Work)
startTime = int(input('Enter starting time: '))
duration = int(input('Enter how long: '))
print('Your event starts at', startTime, "o'clock.")

# Calculate the end time by adding duration to the start time,
# then taking the remainder when divided by 12 to get the time in a 12-hour format.
endTime = (startTime + duration) % 12
print('Your event ends at', endTime, "o'clock.")
# Most Review:

# Count down from 10 to 1 and print "Blast off!" at the end.
for d in range(10, 0, -1):
    print(d)
print("Blast off!")

# Print multiples of 2 for numbers from 5 to 7 (inclusive).
for num in range(5, 8):
    print(num, 2 * num)

# Working with strings

s = "City University of New York"
# Print the character at index 3, and the substring from index 0 to 2 (exclusive).
print(s[3], s[0:3], s[:3])

# Print the substring from index 5 to 7 (exclusive) and the last character.
print(s[5:8], s[-1])

# Iterating through a list of names and printing each name.
names = ["Eleanor", "Anna", "Alice", "Edith"]
for n in names:
    print(n)

# Using the turtle module to draw with a turtle graphics window.
import turtle
teddy = turtle.Turtle()

# Iterate through a list of color names, change the turtle's color, draw, and dot.
names = ["violet", "purple", "indigo", "lavender"]
for c in names:
    teddy.color(c)
    teddy.left(60)
    teddy.forward(40)
    teddy.dot(10)

# Lift the pen, move the turtle forward, and put the pen down.
teddy.penup()
teddy.forward(100)
teddy.pendown()

# Iterate through a list of hexadecimal color codes, change the turtle's color, draw, and dot.
hexNames = ["#FF00FF", "#990099", "#550055", "#111111"]
for c in hexNames:
    teddy.color(c)
    teddy.left(60)
    teddy.forward(40)
    teddy.dot(10)

# Close the turtle graphics window when clicked.
turtle.Screen().exitonclick()

# ⁡⁣⁢⁣Before next lecture, don’t forget to:
# Work on this week’s Online Lab
# Schedule an appointment to take the Quiz in lab 1001G Hunter North
# Schedule an appointment to take the Code Review in lab 1001G
# Hunter North
# Submit this week’s programming assignments
# If you need help, schedule an appointment for Tutoring in lab 1001G
# 11:30am-5pm
# Take the Lecture Preview on Blackboard on Monday (or no later than
# 10 am on Tuesday)⁡