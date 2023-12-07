import pandas as pd
import plotly.express as px

df_6 = pd.read_csv('data/Crimes_6_LaRegions.csv')

df_6['Date_Rptd1'] = pd.to_datetime(df_6['Date_Rptd'], format='%m/%d/%Y %I:%M:%S %p')

df_6['Year'] = df_6['Date_Rptd1'].dt.year
df_6['Month'] = df_6['Date_Rptd1'].dt.month
df_6['Day'] = df_6['Date_Rptd1'].dt.day

#1. Data Clock
fig = px.sunburst(df_6, 
                  path=['Year', 'Month', 'Day'], 
                  title='Crime Frequency (2020-2023) Data Clock')

fig.write_html("LACrime_data_clock.html")

#2. Hotspot map - created using ArcGIS Pro

import arcpy

crime_feature_class = 'Crimes_6_LaRegions.shp'

crime_layer = arcpy.MakeFeatureLayer_management(crime_feature_class, 'crime_layer')

hotspot_result = 'hotspot_result.shp'

arcpy.stats.HotSpots('crime_layer', 'Crime_CD', hotspot_result)

map_document = arcpy.mapping.MapDocument('CURRENT')
data_frame = arcpy.mapping.ListDataFrames(map_document)[0]
hotspot_layer = arcpy.mapping.Layer(hotspot_result)
arcpy.mapping.AddLayer(data_frame, hotspot_layer)
map_document.save()

arcpy.mapping.ExportToPNG(map_document, 'hotspot_map.png', resolution=300)
