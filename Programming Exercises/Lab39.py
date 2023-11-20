#Name: Vansh Bataviya
#Date: October 2023
#Defining Main function that will print Hello World.
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file

coll = pd.read_csv(csvFile)
print(coll["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])