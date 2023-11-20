#Name: Vansh Bataviya
#Date: October 2023
#Defining Main function that will print Hello World.

hour = int(input("Enter hour(in 24 hour time): "))

if hour <= 12:
    print("Good Morning.")
elif hour < 17:
    print("Good Afternoon.")
else:
    print("Good Evening.")