import pandas as pd
import matplotlib.pyplot as plt

merged_data = pd.read_csv('data/Crimes_6_LaRegions.csv')

# Visualization 1: Data Clock
crime_frequency_data = merged_data.groupby(['Year', 'Month']).size().reset_index(name='Crime_Count')
plt.pie(crime_frequency_data['Crime_Count'], labels=crime_frequency_data['Month'], autopct='%1.1f%%')
plt.title('Los Angeles Crime Frequency (2020-2023)')
plt.show()

# Visualization 2: Hotspot Analysis (created using ArcGIS Pro)
![Severe Crime Hotspots](src/utils/hotspot.png)

#Visualization 3: Fishnet Grid (created using ArcGIS Pro)
![Fishnet Grid](src/utils/fishnet.png)

#The following is code written in ArcPy in the ArcGIS Pro Python Notebook. 
#1. Hotspot Analysis: 
#import arcpy
#input_shapefile = "Crimes_6_LaRegions.shp"
#output_hotspot_map = "C:\\Users\\malli\\Documents\\Education\\M.S. Spatial Data Science\\Semester 2\\DSCI 510\\Screenshots\\Severe_Crime_Hotspots.png"
#arcpy.analysis.HotSpots(input_shapefile, output_hotspot_map, "Part_1_2")

#2. Fishnet Grid: 
#import arcpy
#input_shapefile = "Crimes_6_LaRegions.shp"
#output_fishnet_grid = "C:\\Users\\malli\\Documents\\Education\\M.S. Spatial Data Science\\Semester 2\\DSCI 510\\Screenshots\\Fishnet_Grid.png"
#arcpy.management.CreateFishnet(output_fishnet_grid, "xmin", "ymin", "xmax", "ymax", "cell_width", "cell_height", "number_rows", "number_columns", "labels", "geometry_type", "template", "build_polygon")
