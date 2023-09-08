#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/05/2023
#This highlights what was covered in Lec_2

# Review of Lecture 1: turtle graphics
import turtle
t = turtle.Turtle()
#draw side one
t.forward(100)
t.left(120)
#draw side two
t.forward(100)
t.left (120)
#draw side three
t.forward(100)
t. left (120)

# Review of Lecture 1: for-loops

import turtle
t = turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)

# Group Work:
for a in [0,1,2,3,4,5]:
    print(a)

for count in range(6):
    print(count)

for color in ["red", "green", "blue"]:
    print(color)

for i in range(2):
    for j in range(2):
        print("hello from inner loop")
    print("hello from outer loop")

# Range function
for num in [2,4,6,8,10]:
    print(num)

sum = 0
for x in range(0,12,2): ⁡⁣⁢⁣""" This is in the format: range(start, stop, step) """⁡
    print(x)
    sum = sum + x
print(sum)

for c in "ABCD":
    print(c)

#Lecture Slip
words = input("Enter your words in one line:")
num = words.count("s")
print(num)

⁡⁣⁢⁣"""
A variable is a reserved memory location for storing a value.
-> Different kinds, or types, of values need different amounts of space:
    -> int: integer or whole numbers
    -> float: floating point or real numbers
    -> string: sequence of characters
"""⁡
