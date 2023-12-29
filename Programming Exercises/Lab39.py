#Date: 11/15/2023
#This program implements a simple Python script using the Pandas library to read a CSV file, prompt the user for input, and then display the top three contributing factors for vehicle-related incidents from the specified column in the CSV file.
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file

coll = pd.read_csv(csvFile)
print(coll["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])