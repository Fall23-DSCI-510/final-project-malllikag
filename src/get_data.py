import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('superstore.csv')

import requests

def get_coordinates(api_key, city):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': city,
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None

api_key = 'AIzaSyDWK90QN3AbqrwyI3UvFhToYkmHz7jJlPk'
cities = ['Los Angeles', 'San Francisco', 'New York City', 'Philadelphia', 'Santo Domingo']
for city in cities:
    coordinates = get_coordinates(api_key, city)
    if coordinates:
        print(f"Coordinates for {city}: {coordinates}")
    else:
        print(f"Unable to retrieve coordinates for {city}")

