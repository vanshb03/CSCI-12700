#Date: 11/15/2023
#This program implements a simple function, monthString, which takes a numeric input representing a month and returns its corresponding string representation, and the main function that takes user input for a month number, calls the monthString function, and prints the result.


def monthString(monthNum):
     months = ["January", "February", "March", "April",\
            "May", "June", "July", "August", "September", \
            "October", "November", "December"]
  
     return(months[monthNum-1])

def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)

#Allow script to be run directly:
if __name__ == "__main__":
     main()