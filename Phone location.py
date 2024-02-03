import phonenumbers

import folium

from location import number

from phonenumbers import geocoder

key='31be75ab0b9a4e21b6bc5cb86a13d294'

samNumer = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumer,"en")

print(yourLocation)

##get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)

print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

result = geocoder.geocode(query)

##print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))

myMap.save("ExactLocation.html")
