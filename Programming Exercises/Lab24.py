#⁡⁣⁢⁣Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/20/2023
#Write a program that asks the user for a list of nouns (separated by spaces) and approximates the fraction that are plural by counting the fraction that end in "s". 
#Your program should output the total number of words and the fraction that end in "s". Assume that words are separated by spaces (and ignore the possibility of tabs and punctuation between words.)⁡

list = input("Enter nouns: ")
words = list.split()

count = 0

for i in words:
    if i[-1] == "s":
        count = count + 1

print("Number of words: ",len(words))
print("Fraction of your list that is plural is: ",count/len(words))