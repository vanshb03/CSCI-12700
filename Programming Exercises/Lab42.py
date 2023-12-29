#Date: 11/20/2023
#This program implements the creation of an interactive map using the Folium package in Python, centered at latitude 40.75 and longitude -74.125, with a zoom level of 10, and adds a marker for Hunter College at coordinates (40.768731, -73.964915), saving the map as an HTML file named 'nycMap.html.'

#Import the folium package for making maps
import folium

#Create a map, centered (0,0), and zoomed out a bit:
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

#Save the map:
mapCUNY.save(outfile='nycMap.html')