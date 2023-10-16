#Name: Vansh Bataviya
#Date: October 2023
#Defining Main function that will print Hello World.

import numpy as np
from matplotlib import pyplot as plt

inF = input("Enter image file name: ")
outF = input("Enter output file: ")

img = plt.imread(inF) #Read in image from inF
height = img.shape[0] #Get height
width = img.shape[1] #Get width
# 5 Make a new image that’s half the height and half the width.
img2 = img[height//2:, :width//2] #Crop to lower left corner
# Display the new image.
# plt.imshow(img2) #Load our new image into pyplot
# plt.show() #Show the image
plt.imsave(outF, img2)
