import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.holtwinters import ExponentialSmoothing

merged_data = pd.read_csv('data/merged_data.csv')

# Convert 'Date' column to datetime format
merged_data['Date'] = pd.to_datetime(merged_data['Date'])

# Analysis 1: Correlation matrix (Pearson R)
correlation_matrix = merged_data.corr()

# Analysis 2: Demographic Analysis - Bar chart
gender_distribution = merged_data.groupby(['Crime_Code', 'Gender']).size().unstack()
gender_distribution.plot(kind='bar', stacked=True)
plt.title('Distribution of Victims by Gender (Demographic Analysis)')
plt.xlabel('Crime Code')
plt.ylabel('Count')
plt.show()

# Analysis 3: Monthly Crimes per Region - Line graph
regions_of_interest = ['77th Street', 'Central', 'Hollywood', 'Pacific', 'Southwest']
monthly_crimes_per_region = merged_data[merged_data['Region'].isin(regions_of_interest)]
monthly_crimes_per_region = monthly_crimes_per_region.groupby(['Date', 'Region']).size().unstack()

monthly_crimes_per_region.plot(kind='line', marker='o')
plt.title('Monthly Crimes for Hotspot LA Regions (2020-Present Day)')
plt.xlabel('Date')
plt.ylabel('Total Crimes')
plt.legend(title='Region', loc='upper left')
plt.show()

# Analysis 4: Anomaly Detection - Line graph with moving averages
central_region_data = merged_data[merged_data['Region'] == 'Central']
monthly_crimes_central = central_region_data.groupby('Date').size().reset_index(name='Total_Crimes')

# Calculate 2-month and 5-month moving averages for crime frequency in the Central Los Angeles area.
monthly_crimes_central['2-Mo Moving Avg'] = monthly_crimes_central['Total_Crimes'].rolling(window=2).mean()
monthly_crimes_central['5-Mo Moving Avg'] = monthly_crimes_central['Total_Crimes'].rolling(window=5).mean()

monthly_crimes_central.plot(x='Date', y=['Total_Crimes', '2-Mo Moving Avg', '5-Mo Moving Avg'], marker='o')
plt.title('Monthly Crimes Central')
plt.xlabel('Date')
plt.show()
