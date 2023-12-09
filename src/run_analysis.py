#Univariate Analysis 
#1. Descriptive statistics 
print("\nDescriptive Statistics:")
print(df_clean.describe())

#2. Histogram for market distribution
df_clean['Market'].hist(bins=20)
plt.title('Market Distribution')
plt.xlabel('Market')
plt.ylabel('Frequency')
plt.show()

#Bivariate Analysis 
#1. Correlation analysis 
correlation_matrix = df_clean.corr()
plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', linewidths=.5, fmt=".2f", annot_kws={"size": 10})
plt.title('Correlation Heatmap')
plt.show()

#2. Pair plot 
plt.figure(figsize=(8,6))
pair_plot = sns.pairplot(data=df_clean[['Ship.Mode', 'Quantity', 'Profit', 'Sales', 
                                  'Shipping.Cost']].sample(1000), hue='Ship.Mode',
           height=6)
plt.plot();
