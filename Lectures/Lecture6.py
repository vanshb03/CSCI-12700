#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/19/2023
#This highlights what was covered in Lec_6

#Recap: Logical Operators:
    # Logical Expressions
    # Circuits
    # Binary Numbers
    # 
# and
    # in1 in2 returns:
    # False and False False
    # False and True False
    # True and False False
    # True and True True

# or
    # in1 in2 returns:
    # False or False False
    # False or True True
    # True or False True
    # True or True True

# not
    # in1 returns:
    # not False True
    # not True False

#Group Work: Design Question
# Design a program that asks the user for an image and then display the upper left quarter of the image. (First, design the pseudocode, and if time, expand to a Python program.)

# How to approach this:
# Create a “To Do” list of what your program has to accomplish.
# Read through the problem, and break it into “To Do” items.
# Don’t worry if you don’t know how to do all the items you write down.
# Example:
    # 1 Import libraries.
    # 2 Ask user for an image name.
    # 3 Read in image.
    # 4 Figure out size of image.
    # 5 Make a new image that’s half the height and half the width.
    # 6 Display the new image.

# Import libraries.
import matplotlib.pyplot as plt
import numpy as np
# 2 Ask user for an image name.
inF = input("Enter file name: ")
# 3 Read in image.
img = plt.imread(inF) #Read in image from inF
# 4 Figure out size of image.
height = img.shape[0] #Get height
width = img.shape[1] #Get width
# 5 Make a new image that’s half the height and half the width.
img2 = img[height//2:, :width//2] #Crop to lower left corner
# Display the new image.
plt.imshow(img2) #Load our new image into pyplot
plt.show() #Show the image

#Structured Data:
# Common to have data structured in a spread sheet.
# In the example above, we have the first line that says “Undergraduate”.
# Next line has the titles for the columns.
# Subsequent lines have a college and attributes about the college.
# Python has several ways to read in such data.
# We will use the popular Python Data Analysis Library (Pandas).

# We will use the popular Python Data Analysis Library (Pandas).
# Open source and freely available (part of anaconda distribution).
# See Lab 1 for directions on downloading it to your home machine.
# If you can’t install on your computer, it is supported in
# https://repl.it/
# To use, add to the top of your program:
import pandas as pd

# Excel .xls files have much extra formatting.
# The text file version is called CSV for comma separated values.
# Each row is a line in the file.
# Columns are separated by commas on each line.

# Reading in CSV Files
# To read in a CSV file: 
myVar = pd.read csv("myFile.csv")
# Pandas has its own type, DataFrame, that is perfect for holding a sheet of data.
# Often abbreviated: df.
# It also has Series, that is perfect for holding a row or column of data.

import matplotlib.pyplot as plt
import pandas as pd
pop = pd.read_csv("nycHistPop.csv",skiprows=5)
pop.plot(x="Year")
plt.show()

# Series in Pandas
# Series can store a column or row of a DataFrame.
# Example: pop["Manhattan"] is the Series corresponding to the column of
# Manhattan data.
# Example:
print("The largest number living in the Bronx is",
pop["Bronx"].max())

# Predict what the following will do:
    # print("Queens:", pop["Queens"].min())
        # Minimum value in the column with label “Queens”.
    # print("S I:", pop["Staten Island"].mean())
        # Average of values in the column “Staten Island”.
    # print("S I:", pop["Staten Island"].std())
        # Standard deviation of values in the column “Staten Island”
    # pop.plot.bar(x="Year")
        # Bar chart with x-axis ”Year”.
    # pop.plot.scatter(x="Brooklyn", y= "Total")
        # Scatter plot of Brooklyn versus Total values.
    # pop["Fraction"] = pop["Bronx"]/pop["Total"]
        # New column with the fraction of population that lives in the Bronx.

#Challenge:
# Write a complete Python program that reads in the file, cunyF2016.csv, and produces a scatter plot of full-time versus part-time enrollment.

import matplotlib.pyplot as plt
import pandas as pd
pop = pd.read_csv("cunyF2016.csv")
pop.plot.scatter(x="Full-time",y="Part-time")
plt.show()

#Groupby()
# Sometimes you have recurring values in a column and you want to examine the data for a particular value.
# For example, to find the average rainfall at each location:
    # 1 Import libraries.
import pandas as pd
    # 2 Read in the CSV file.
rain =
pd.read_csv("AustraliaRain.csv",skiprows=1)
    # 3 Group the data by location.
groupAvg =
rain.groupby("Location")
    # 4 Print the average rainfall at each location.
print(groupAvg["Rainfall"].mean())

#get_group()
# Sometimes you have recurring values in a column and you want to examine the data for a particular value.
# For example, to find the average rainfall at
# one location, e.g. Albury:
    # 1 Import libraries.
import pandas as pd
    # 2 Read in the CSV file.
rain = pd.read_csv("AustraliaRain.csv",skiprows=1)
    # 3 Group the data by location get data for group Albury.
AlburyAvg = rain.groupby("Location").get_group("Albury")
    # 4 Print the average rainfall in Albury.
print(AlburyAvg["Rainfall"].mean())

#Design Challenge:
# Design an algorithm that:
    # Prints the luminosity of the brightest star.
    # Prints the temperature of the coldest star.
    # Prints the average radius of a Hypergiant.
# Libraries: pandas
# Process:
    # Print max of ’Luminosity’ column
    # Print min of ’Temperature’ column
    # groupby ’Star Type’ and take averages, then print max of ’Radius’ column
    # OR groupby ’Star Type’ and get group ’Hypergiant’ to print average ’Radius’

#Design Challenge Code:
# Libraries: pandas
import pandas as pd
stars = pd.read csv("Stars.csv")
# Process:
    # Print max of ’Luminosity’ column
print(stars["Luminosity(L/Lo)"].max())
    # Prints min of ’Temperature’ column and store it in temp variable
print( stars["Temperature (K)"].min())
    # OR groupby ’Star Type’ and get group ’Hypergiant’ to print average ’Radius’
print(stars.groupby("Star type")\
.get group("Hypergiant").mean()["Radius(R/Ro)"])

#Recap:
# Recap: Logical Expressions & Circuits
# Accessing Formatted Data:
    # Pandas library has elegant solutions for accessing & analyzing structured data.
    # Can manipulate individual columns or rows (’Series’).
    # Has useful functions for the entire sheet (’DataFrame’) such as plotting.