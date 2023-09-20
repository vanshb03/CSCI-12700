#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/20/2023
#This program implements the pseudocode below:

# 1.  Ask the user for the number of hours until the weekend.
# 2.  Print out the days until the weekend (days = hours // 24)
# 3.  Print out the leftover hours (leftover = hours % 24)

hours = int(input("Enter number of hours: "))
days = hours // 24
print("Days:",days)
leftover = hours % 24
print("Hours:",leftover)