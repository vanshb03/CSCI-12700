#Name: Vansh Bataviya
#Date: October 2023
#Defining Main function that will print Hello World.


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