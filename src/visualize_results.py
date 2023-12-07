import pandas as pd
import matplotlib.pyplot as plt

merged_data = pd.read_csv('data/Crimes_6_LaRegions.csv')

# Visualization 1: Data Clock
crime_frequency_data = merged_data.groupby(['Year', 'Month']).size().reset_index(name='Crime_Count')
plt.pie(crime_frequency_data['Crime_Count'], labels=crime_frequency_data['Month'], autopct='%1.1f%%')
plt.title('Los Angeles Crime Frequency (2020-2023)')
plt.show()

# Visualization 2: Hotspot Analysis (created using ArcGIS Pro)

#Visualization 3: Fishnet Grid (created using ArcGIS Pro)
