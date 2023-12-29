#Date: 10/05/2023
#This program implements a simple Python script using Matplotlib and Pandas to visualize the population fraction of a specified borough in New York City over the years and saves the resulting plot as an image.

import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter borough name: ")
output = input("Enter image name: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop['Fraction'] = pop[name]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')
fig = plt.gcf()
fig.savefig(output)