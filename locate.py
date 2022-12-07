from geopy.geocoders import Nominatim
import json

# Initialize API
geolocator = Nominatim(user_agent="MyApp")

file = open('FileNames.json')
entries = json.load(file)

for entry in entries:
    print(entry["City"])
# location = geolocator.geocode("Cochin")
# print("The latitude of the location is: ", location.latitude)
# print("The longitude of the location is: ", location.longitude)