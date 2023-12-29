#Date: 10/20/2023
#This program implements a simple Python code that takes a user-inputted list of names separated by semicolons, splits the names into individual entries, and then prints each name with its last name followed by a comma and first name.

list = input("Please enter your list of names : ")
colon = list.split("; ")
for post in colon:
    comma = post.split(", ")
    print(comma[1], comma[0])