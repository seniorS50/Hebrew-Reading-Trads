import json
import re
import sqlite3
# importing geopy library
from geopy.geocoders import Nominatim
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
f = open('filenames.json')
filedicts = json.load(f)
f.close()
cities = []
citytracker = []
for file in filedicts:
    city = file["City"].replace("_"," ")
    city = city.capitalize()
    if city not in citytracker:
        country = file["Country"].replace("_"," ")
        getLoc = loc.geocode(city)
        if getLoc:
            # printing address
    #        print(city + ":")
            # printing latitude and longitude
            lat = getLoc.latitude
            long = getLoc.longitude
        else:
            print("Problem with: " + city)
        entry = {"Country": country, "City": city, "Latitude": lat, "Longitude": long}
        cities.append(entry)
        citytracker.append(city)

with open("city_locs.json", "w") as final:
   json.dump(cities, final)

# sort        
# cities.sort()
# # replace _ with spaces
# for city in cities:
#     city = city.replace("_", " ")
# # Check if the city is already there
#     if city not in cities["City"]    
# # entering the location name
#     getLoc = loc.geocode(city)
#     if getLoc:
#         # printing address
#         print(city + ":")
#         # printing latitude and longitude
#         print("Latitude = ", getLoc.latitude)
#         print("Longitude = ", getLoc.longitude, "\n")
#     else:
#         print("Problem with: " + city)
