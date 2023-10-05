#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 10/05/2023
#Build a circuit that has the same behavior as a nand gate (i.e. for the same inputs, gives identical output) using only and, or, and not gates.
#It doesn't run bozo

import matplotlib.pyplot as plt
import pandas as pd

name = input("Enter borough name: ")
output = input("Enter borough name: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop['Fraction'] = pop[name]/pop['Total']
pop.plot(x = 'Year', y = 'Fraction')
fig = plt.gcf()
fig.savefig(output)