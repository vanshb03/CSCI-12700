#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/05/2023
#This program will prompt the user to enter a phrase and then prints out the ASCII code of each character in the phrase.

phrase = input("Enter a phrase:")

print("In ASCII:")
for c in phrase:
    print(ord(c))