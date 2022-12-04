import json
import re
import sqlite3
# importing geopy library
from geopy.geocoders import Nominatim
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
f = open('filenames.json')

filedicts = json.load(f)
cities = []
for file in filedicts:
    city = file["City"].replace("_"," ")
    city = city.capitalize()

    if file["City"] not in cities:
        cities.append(file['City'])
# sort        
cities.sort()
# replace _ with spaces
for city in cities:
    city = city.replace("_", " ")    
# entering the location name
    getLoc = loc.geocode(city)
    if getLoc:
        # printing address
        print(city + ":")
        # printing latitude and longitude
        print("Latitude = ", getLoc.latitude)
        print("Longitude = ", getLoc.longitude, "\n")
    else:
        print("Problem with: " + city)
