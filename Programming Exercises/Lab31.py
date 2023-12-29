#Date: 09/20/2023
#This program implements a Python script using the pandas and matplotlib libraries to read a CSV file containing homeless shelter data, calculate the fraction of children in the shelters, and generate a time-series plot of this fraction, ultimately saving the plot as an image file based on user-specified input and output file names.

import matplotlib.pyplot as plt
import pandas as pd

inF = input("Enter name of input file: ")
outF = input("Enter n ame of output file: ")

homeless = pd.read_csv(inF)
homeless["Fraction Children"] = homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")
fig = plt.gcf()
fig.savefig(outF)
