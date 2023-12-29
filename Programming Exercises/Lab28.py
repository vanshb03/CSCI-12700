#Date: 10/05/2023
#This program implements a Python script that uses the matplotlib and pandas libraries to visualize and analyze historical population data for New York City boroughs, prompting the user to input a specific borough name and then displaying the average and maximum population for that borough.

import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter borough name: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print("Average Population: ", pop[name].mean())
print("Max Population: ", pop[name].max())