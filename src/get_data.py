import pandas as pd 
import numpy as np 
import requests 

def get_population_data():
  pop_data = pd.read_csv('C:\Users\malli\Documents\Education\M.S. Spatial Data Science\Semester 3\SSCI 575\Final Project\LA_Crimes\CSV Files\ca_zip_pop.csv')
  pop_data = pop_data.groupby('zipcode').agg({'population': 'max'}).reset_index()
  ca_zips = pd.read_csv('C:\Users\malli\Documents\Education\M.S. Spatial Data Science\Semester 3\SSCI 575\Final Project\LA_Crimes\CSV Files\ca_zip_pop.csv'
  pop_zip = pop_data.merge(ca_zips, how='inner', left_on='zipcode', right_on='ZIP_CODE')
  return pop_zip

def get_lat_lng_coordinates(pop_zip):
  lat, lng = [], []

  for idx in range(len(pop_zip)):
    print(idx)
    api_key = 'AIzaSyBziINbv_qWJy83YUIG4_cwRGvnFiCSHNg'
    zip_code = pop_zip['ZIP_CODE'].iloc[idx]
    api_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={zip_code}&key={api_key}'

    response = requests.get(api_url)
    print(response)
    data = response.json()

    #Extract coordinates
    try: 
      coords = data['results'][0]['geometry']['location']
      lat.append(coords['lat'])
      lng.append(coords['lng'])
    except:
      lat.append(np.nan)
      lng.append(np.nan)

  return lat, lng

def main():
  population_data = get_population_data()
  latitudes, longitudes = get_lat_lng_coordinates(population_data)

  population_data['latitude'] = latitudes
  population_data['longitude'] = longitudes

  population_data.to_csv('data/raw/population_data_with_coordinates.csv', index=False)

if __name__=="__main__":
  main()
    
