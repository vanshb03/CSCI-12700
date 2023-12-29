#Date: 09/20/2023
#This program implements a string manipulation script that generates substrings of an input string 's' by iteratively printing its prefixes and suffixes, followed by a concluding message.

s = input("Enter string:")
ls = len(s)
for i in range(0,ls):
    print(s[:i])
for i in range(0,ls):
    print(s[i:])

print("Thank you for using my program!")