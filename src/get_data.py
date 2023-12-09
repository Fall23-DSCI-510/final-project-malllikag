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

coord_dic = {}
for city in df.City.unique():
    coordinates = get_coordinates(api_key, city)
    if coordinates:
        print(f"Coordinates for {city}: {coordinates}")
        coord_dic[city] = [coordinates[0], coordinates[1]]
    else:
        print(f"Unable to retrieve coordinates for {city}")

