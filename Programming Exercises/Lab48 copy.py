#Date: 12/01/2023
#Defining Main function that will print Hello World.

# Modified by: Vansh

def mystery(num):
  send = chr(num)
  if num < ord("k"):
    send = send + send
  return send
def enigma(letters):
  mess = ""
  for l in letters:
    n = ord(l)
    c = mystery(n)
    mess = mess + c
  return mess
word = input("Enter a word: ")
s = enigma(word)
print("Output is:", s)