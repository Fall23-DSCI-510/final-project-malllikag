# Display basic information about the dataset
print("Original DataFrame:")
print(df.info())

# Handling Missing Values
df.dropna(inplace=True)

# Removing Duplicates
df.drop_duplicates(inplace=True)

# Convert Date column to datetime format
df['Order.Date'] = pd.to_datetime(df['Order.Date'])

# Extract Year and Month from the OrderDate
df['Year'] = df['Order.Date'].dt.year
df['Month'] = df['Order.Date'].dt.month

# Display cleaned DataFrame
print("\nCleaned DataFrame:")
print(df.head())

df.to_csv('cleaned_superstore.csv', index=False)
