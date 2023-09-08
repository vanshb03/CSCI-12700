#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/05/2023
#This program will prompts the user to enter a word and then prints out the word with each letter shifted right by 13. 
#That is, 'a' becomes 'n', 'b' becomes 'o', ... 'y' becomes 'l', and 'z' becomes 'm'.

word = input("Enter a word:")
codedWord = ""
for ch in word:
    offset = ord(ch) - ord('a') + 13 #how many letters past 'a'
    wrap = offset % 26  #if larger than 26, wrap back to 0
    newChar = chr(ord('a') + wrap)  #compute the new letter
    # print(wrap, chr(ord('a') + wrap))    #print the wrap & new letter
    codedWord = codedWord + newChar #add the newChar to the coded word
print("Your word in code is:", codedWord)

# phrase = input("Enter a word:")
# newMessage = ""

# for a in phrase:

#     if ord(a) + 13 >= 122:
#         newMessage += chr(ord(a) - 26 + 13)

#     else:
#         newMessage += chr(ord(a) + 13)

# print("Your word in code is:", newMessage)