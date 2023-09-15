#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/12/2023
#This highlights what was covered in Lec_3

#More on Strings: Indexing & Substrings
s = "FridaysSaturdaysSundays"
days = s[7]
print(days)
days = s[7:15]
print(days)
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

endTime = (startTime+duration)%12
print('Your event ends at', endTime, "o'clock.")

# Most Review:
for d in range(10, 0, -1): 
    print(d) 
print("Blast off!")

for num in range(5,8): 
    print(num, 2*num)

s = "City University of New York" 
print(s[3], s[0:3], s[:3])
print(s[5:8], s[-1])

names = ["Eleanor", "Anna", "Alice", "Edith"]
for n in names:
    print(n)

import turtle
teddy= turtle.Turtle()

names = ["violet", "purple", "indigo", "lavender"]
for c in names:
    teddy.color(c)
    teddy.left(60)
    teddy.forward(40) 
    teddy.dot(10)

teddy.penup()
teddy.forward(100)
teddy.pendown()

hexNames = ["#FF00FF", "#990099", "#550055", "#111111"]
for c in hexNames:
    teddy.color(c)
    teddy.left(60)
    teddy.forward(40)
    teddy.dot(10)

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