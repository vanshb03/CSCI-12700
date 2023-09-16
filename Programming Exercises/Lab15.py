#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/05/2023
#This program will print each character of the word reverse twice with a space gap in between.

main = input("Enter a word.")
val = main[::-1]
for char in range(0, len(main)):
   print(val[char],val[char])
