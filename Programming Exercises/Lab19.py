#Date: 09/20/2023
#This program implements the pseudocode below:

# The program asks the user for the number of hours input until the weekend.
# The program then prints out the days until the weekend (days = hours // 24)
# The program then prints out the leftover hours (leftover = hours % 24)

hours = int(input("Enter number of hours: "))
days = hours // 24
print("Days:",days)
leftover = hours % 24
print("Hours:",leftover)