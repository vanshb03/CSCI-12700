#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/13/2023
#This program changes the color of a picture using matplotlib.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

file1 = input("Enter name of the input file: ")
file2 = input("Enter name of the output file: ")
img = plt.imread(file1)   #Read in image from csBridge.png
# plt.imshow(img)		                 #Load image into pyplot
# plt.show()

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0           #Set the blue channel to 0

# plt.imshow(img2)         #Load our new image into pyplot
# plt.show()               #Show the image (waits until closed to continue)

plt.imsave(file2, img2)  #Save the image we created to the file: reds.png                         #Show the image (waits until closed to continue)