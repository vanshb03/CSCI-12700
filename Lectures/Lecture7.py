#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 10/17/2023
#This highlights what was covered in Lec_7

#Functions:
    # Functions are a way to break code into pieces, that can be easily reused.
    # Many languages require that all code must be organized with functions.
    # The opening function is often called main()
    # Naming conventions same as variables
    # You call or invoke a function by typing its name, followed by any inputs, surrounded by parenthesis:
    # Example: print("Hello", "World")
    # Can write, or define your own functions, which are stored, until invoked or called.

# “Hello, World!” with Functions
    #This program, uses functions, says hello to the world!
def main():
    print("Hello, World!")
if __name__ == "__main__":
    main()

# Challenge: Predict what the code will do
    # Code1
def totalWithTax(food, tip):
    tax = 0.1 * food
    return(food + tax + tip)
lunch = float(input("Enter lunch total: "))
l_tip = float(input("Enter lunch tip: " ))
l_total = totalWithTax(lunch, l_tip)
print("Lunch total is", l_total)

    # Code2
def totalWithTax(food, tip):
    tax = 0.1 * food
    return(food + tax + tip)
dinner = float(input("Enter dinner total: "))
d_tip = float(input("Enter dinner tip: " ))
d_total = totalWithTax(dinner, d_tip)
print("Dinner total is", d_total)

#Scope:
def eight():
    x = 5 + 3
    print(x)

def nine():
    x = "nine"
    print(x)

# You can have multiple functions.
# Each function defines the scope of its local variables
# A variable defined inside a function is local, i.e. defined only inside that function.

#Input Parameters & Return Values:
    # Functions can have input parameters.
    # Surrounded by parentheses, both in the function definition, and in the function call(invocation).
    # The “placeholders” in the function definition: formal parameters.
    # The ones in the function call: actual parameters.
    # Functions can also return values to where it was called.


def prob4():
    verse = "jam jam tomorrow and jam yesterday,"
    print("The rule is,")
    c = mystery(verse)
    w = enigma(verse,c)
    print(c,w)

def mystery(v):
    print(v)
    c = v.count("jam")
    return(c)
1
def enigma(v,c):
    print("but never", v[-1])
    for i in range(c):
        print("jam")
    return("day.")

prob4()

#Lecture Slip Question 3:
def month_string(month_num):
  months = ["January", "February", "March", "April",\
            "May", "June", "July", "August", "September", \
            "October", "November", "December"]
  
  return(months[month_num-1])


def main():
   n = int(input("Enter the number of the month: "))
   month_name = month_string(n)
   print("The month is", month_name)

main()

#GitHub:
    # Used to collaborate on and share code, documents, etc.
    # Supporting Open-Source Software: original source code is made freely available and may be redistributed and
    # modified.
    # More formally: git is a version control protocol for tracking changes and versions of documents.
    # GitHub provides hosting for repositories (‘repos’) of code.
    # Also a convenient place to host websites(e.g. huntercsci127.github.io).

#Recap Functions:
    # Functions are a way to break code into pieces, that can be easily reused.
    # You call or invoke a function by typing its name,
    # followed by any inputs, surrounded by parenthesis:
    # Example: print("Hello", "World")
    # Can write, or define your own functions, which are stored, until invoked or called.

# Accessing Structured Data: NYC Open Data
    # Freely available source of data.
    # Maintained by the NYC data analytics team.
    # We will use several different ones for this class.
    # Will use pandas, pyplot & folium libraries to analyze, visualize and map the data.
    # Lab 7 covers accessing and downloading NYC OpenData datasets.

# Recap: Slicing & Images
import matplotlib.pyplot as plt
import numpy as np
height= 20
width = 30
#An image is an array with height, width and
#depth 3 for the red, green, and blue channels
img = np.zeros((height, width, 3))
img[:height//2, :width//2, 0] = 1 #upper left corner
img[height//2:, :width//2, 1] = 1 #lower left corner
img[:height//2:2, width//2:, 2] = 1 #upper right corner
img[height//2:, width//2::2, :2] = 1 #lower right corner
plt.imshow(img)
plt.show()
