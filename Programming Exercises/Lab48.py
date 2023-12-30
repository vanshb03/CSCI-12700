#Date: 12/01/2023
#This program implements a loop that prompts the user to enter a non-empty string, continually requesting input until a non-empty string is provided, and then prints the entered string.

word = input("Enter a non-empty string:")

while word == "":
  print("That was empty. Try again.")
  word = input("Enter a non-empty string:")

print("You entered:",word)