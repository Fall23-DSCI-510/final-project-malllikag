import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_crime_data(crime_data_file):
    crime_df = pd.read_csv(data/processed/Crimes_6_LaRegions)

    # 1. Demographic Analysis: Bar chart representing distribution of victims by gender
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Victim_Gender', data=crime_df, palette='pastel')
    plt.title('Distribution of Victims by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.savefig('results/victims_distribution_by_gender.png')
    plt.show()

    # 2. Regional Analysis: Monthly crimes per region
    region_monthly_crimes = crime_df.groupby(['Region', 'YearMonth'])['Crime_Type'].count().reset_index()
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='YearMonth', y='Crime_Type', hue='Region', data=region_monthly_crimes)
    plt.title('Monthly Crimes per Hotspot LA Region (2020-Present Day)')
    plt.xlabel('Date')
    plt.ylabel('Total Crimes')
    plt.savefig('results/monthly_crimes_per_region.png')
    plt.show()

    # 3. Anomaly Detection: Monthly crimes in Central region with 2 and 5 month moving averages
    central_region_crimes = crime_df[crime_df['Region'] == 'Central']
    central_region_crimes['Date'] = pd.to_datetime(central_region_crimes['Date'])
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='Date', y='Crime_Type', data=central_region_crimes, label='Monthly Crimes')
    sns.lineplot(x='Date', y='Crime_Type', data=central_region_crimes.rolling(window=8).mean(), label='2 Month Avg')
    sns.lineplot(x='Date', y='Crime_Type', data=central_region_crimes.rolling(window=20).mean(), label='5 Month Avg')
    plt.title('Monthly Crimes - Central Region')
    plt.xlabel('Date')
    plt.ylabel('Crime Count')
    plt.legend()
    plt.savefig('results/monthly_crimes_central_region.png')
    plt.show()

crime_data_file_path = 'data/processed/Crimes_6_LaRegions'
analyze_crime_data(crime_data_file_path)
