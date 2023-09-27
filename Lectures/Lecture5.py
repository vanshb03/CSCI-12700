#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/19/2023
#This highlights what was covered in Lec_4

#Group Work 1
import numpy as np
from matplotlib import pyplot as plt

img = np.ones( (10,10,3) )
img[0:10,0:5,0:2] = 0

plt.imsave("img.png",img)

#Group Work 2
num = int(input("Enter size "))
img2 = np.ones( (num,num,3) )
img2[::2,:,1:] = 0

plt.imsave("img2.png",img2)

#Group Work 3
img3 = np.zeros( (100,100,3) )
img3[::2,::2,0] = 1

plt.imsave("img3.png",img3)

#Today's Topics
    # Logical Expressions
    # Circuits
    # Binary Numbers
    # 
# and
    # in1 in2 returns:
    # False and False False
    # False and True False
    # True and False False
    # True and True True

# or
    # in1 in2 returns:
    # False or False False
    # False or True True
    # True or False True
    # True or True True

# not
    # in1 returns:
    # not False True
    # not True False

#Binary Numbers:
    # Logic → Circuits → Numbers
    # Digital logic design allows for two states:
        # I True / False
        # I On / Off (two voltage levels)
        # I 1 / 0
    # Computers store numbers using the Binary system (base 2)
    # A bit (binary digit) being 1 (on) or 0 (off)

#Binary Numbers Continued:
# Two digits: 0 and 1
# Each position is a power of two
    # I Decimal: the ”ones”, ”tens”, ”hundreds” and so on (powers of 10)
    # I Binary: the ”ones”, ”twos”, ”fours”, ”sixteens” and so on (powers of 2)
# In each position the digit is either 0 or 1, so given a binary number we
# can obtain the decimal equivalent as follows:
    # I In the ”ones” position we either have a 1 or not
    # I In the ”twos” position we either have a 2 or not
    # I In the ”fours” position we either have a 4 or not ...
# Example:
    # 11001 in base2 = 16 + 8 + 1 = 25 in base10

#Recap
# In Python, we introduced:
    # I Decisions
    # I Logical Expressions
    # I Circuits
    # I Binary Numbers

#Final Exam:
    # Since you must pass the final exam to pass the course, we end every
    # lecture with final exam review.
    # Pull out something to write on (not to be turned in).
    # Lightning rounds:
        # I write as much you can for 60 seconds;
        # I followed by answer; and
        # I repeat.
    # Past exams are on the webpage (under Final Exam Information)
