[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Z1npak42)

Project Title: Analyzing the Impact of Green Spaces on Urban Temperature in Los Angeles 

Overview: 
This project investigates the relationship between green spaces and urban temperature in Los Angeles. It aims to understand how the presence and distribution of green areas influence local micorclimates and temperature variations. This will be achieved through data collection, data cleaning, data analysis, and finally, data visualization. 

1. Data Collection:
   - Green Space Data: The file 'get_green_space_data.py', located in the data/raw folder collects data on green spaces in Los Angeles. This script scrapes information about the location, size, and type of green spaces and stores it in the data/raw folder.
   - Temperature Data: The file 'get_temperature_data.py', also located in the data/raw folder, collects historic temperature data from the NOAA (National Oceanic and Atmospheric Administration)'s online data search portal and stores it in the data/raw folder.
  
2. Data Cleaning:
   - Green Space Data: The script 'clean_green_space_data.py', located in the data/processed folder, cleans and preprocesses the green space data/ This script handles missing values, data format discrepancies, and inconsistencies.
   - Temperature Data: The script 'clean_temperature_data.py' addresses missing values, date formatting, and data format issues in the scraped temperature data.
  
3. Data Analysis:
Run the analysis script, 'run_analysis.py', to conduct spatial analysis of the relationship between green spaces and temperature. This script calculates temperature differences, assesses correlations, and performs statistical analyses using NumPy and Pandas.

4. Data Visualization:
- The file 'visualizations.py' generates static visualizations such as:
   - Chloropleth maps illustrating temperature variations across Los Angeles
   - Scatterplots or heatmaps depicting the relationship between green space metrics and temperature.
   - This file is saved in the results folder.
 
5. Final Report:
The final report is stored in the results folder and provides a detailed overview of the project, including data collection, analysis, and visualizations. It offers insights into the impact of green spaces on urban temperature in Los Angeles. 
