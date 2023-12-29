#Date: 10/20/2023
#This program implements a simple greeting system based on user-inputted hours in 24-hour format, displaying "Good Morning" if the input is before or equal to 12, "Good Afternoon" if it's between 12 and 17, and "Good Evening" for any later hours.

hour = int(input("Enter hour(in 24 hour time): "))

if hour <= 12:
    print("Good Morning.")
elif hour < 17:
    print("Good Afternoon.")
else:
    print("Good Evening.")