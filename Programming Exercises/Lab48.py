#Name: Vansh Bataviya
#Date: November 2023
#Defining Main function that will print Hello World.

# Modified by: Vansh

word = input("Enter a non-empty string:")

while word == "":
  print("That was empty. Try again.")
  word = input("Enter a non-empty string:")

print("You entered:",word)