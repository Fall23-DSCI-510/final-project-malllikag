#1. Bar chart 
market_data = df_clean.groupby('Market').agg({'Profit': sum, 'Sales': sum}).sort_values(by='Profit', ascending=False).reset_index()

plt.figure(figsize=(12, 6))
#Profit
plt.bar(market_data['Market'], market_data['Profit'], label='Profit')
# Sales
plt.bar(market_data['Market'], market_data['Sales'], bottom=market_data['Profit'], label='Sales')

plt.xlabel('Market')
plt.ylabel('Amount')
plt.title('Profit & Sales across Markets')
plt.legend()
plt.show()

#2. Line plot 
#Monthly sales by Market
mkt_data = df_clean.groupby(['Market', 'Order.Date']).agg({'Sales':'sum'}).reset_index()
plt.figure(figsize=(24,10))
idx, color_ls = 0, ['g', 'r', 'b', 'm', 'k', 'c', 'y'] 
for mkt in mkt_data['Market'].unique():
    area_data = mkt_data[mkt_data['Market'] == mkt]
    plt.plot(area_data['Order.Date'], area_data['Sales'], f'o--{color_ls[idx]}', label=mkt, alpha=0.9,)
    idx+=1
    
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Monthly Sales by Market')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1));

#3. Pie Chart 
#Sales by Regions
region_sales = df_clean.groupby('Region')['Sales'].sum()

plt.figure(figsize=(10, 10))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Sales by Region');

#4. Folium map
import folium
import pandas as pd

map_center = list(coord_dic.values())[0]
my_map = folium.Map(location=map_center, zoom_start=4)

merged_df = pd.merge(df, pd.DataFrame(list(coord_dic.items()), columns=['City', 'Coordinates']), on='City', how='inner')

sales_grouped = merged_df.groupby('City')['Sales'].sum().reset_index()

sales_colors = folium.StepColormap(
    colors=['yellow', 'orange', 'red'],
    vmin=sales_grouped['Sales'].min(),
    vmax=sales_grouped['Sales'].max(),
    index=[sales_grouped['Sales'].quantile(0.33), sales_grouped['Sales'].quantile(0.66)]
)

for index, row in sales_grouped.iterrows():
    coordinates = coord_dic.get(row['City'])
    if coordinates:
        folium.CircleMarker(
            location=coordinates,
            radius=10,
            color=sales_colors(row['Sales']),
            fill=True,
            fill_color=sales_colors(row['Sales']),
            fill_opacity=0.7,
            popup=f"{row['City']}\nAggregated Sales: ${row['Sales']}"
        ).add_to(my_map)

sales_colors.caption = 'Aggregated Sales Distribution'
my_map.add_child(sales_colors)

my_map.save("all_cities_aggregated_sales_map.html")
my_map
