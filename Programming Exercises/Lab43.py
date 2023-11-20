#Name: Vansh Bataviya
#Date: October 2023
#Defining Main function that will print Hello World.

#Import the folium package for making maps
import folium
import pandas as pd

inF = input('Enter input filename:')
outF = input('Enter output filename:')

collisions = pd.read_csv(inF)
collisions["LATITUDE"] = collisions["LATITUDE"].fillna(0)
collisions["LONGITUDE"] = collisions["LONGITUDE"].fillna(0)

mapCrash = folium.Map(location = [40.768731, -73.964915])

for index, row in collisions.iterrows():
    if row['LATITUDE'] != 0 and row['LONGITUDE'] != 0:
		
		## YOUR CODE HERE ##
        #LAT, LONG
        folium.Marker(location = [row['LATITUDE'], row['LONGITUDE']]).add_to(mapCrash)

mapCrash.save(outfile=outF)