#Name: Vansh Bataviya
#Date: October 2023
#Defining Main function that will print Hello World.

#Import the folium package for making maps
import folium

#Create a map, centered (0,0), and zoomed out a bit:
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

#Save the map:
mapCUNY.save(outfile='nycMap.html')