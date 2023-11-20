#Name: Vansh Bataviya
#Date: October 2023
#Defining Main function that will print Hello World.

list = input("Please enter your list of names : ")
colon = list.split("; ")
for post in colon:
    comma = post.split(", ")
    print(comma[1], comma[0])