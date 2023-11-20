#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/20/2023
#

import matplotlib.pyplot as plt
import pandas as pd

inF = input("Enter name of input file: ")
outF = input("Enter name of output file: ")

homeless = pd.read_csv(inF)
homeless["Fraction Children"] = homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")
fig = plt.gcf()
fig.savefig(outF)
