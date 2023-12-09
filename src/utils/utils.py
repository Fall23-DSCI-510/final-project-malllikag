#Multiple Linear Regression
#Prediction of Shipping Cost 

#Identify Associated Features
df.corr()[['Shipping.Cost']].sort_values(by='Shipping.Cost', ascending=False).iloc[1:,0]

map_ = {
    'Critical':4,
    'High':3,
    'Medium':2,
    'Low':1   
}

#Encode Categorical Variables for regression
df['Order.Priority'] = df['Order.Priority'].map(map_)
df['Ship.Mode'] = df['Ship.Mode'].astype('category').cat.codes

import statsmodels.api as sm

X = df[['Sales', 'Profit', 'Quantity', 'Order.Priority']]
Y = df['Shipping.Cost']

#OLS Model
ols_model = sm.OLS(Y, sm.add_constant(X))
 
results = ols_model.fit(cov_type='HAC', cov_kwds={'maxlags': 5})
print(results.summary()) 

df['ShippingC_Pred'] = results.predict(sm.add_constant(X)) #Predictions Stored in DF

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

#Performance Evaluation of Model
pd.DataFrame({'MAPE': [mean_absolute_percentage_error(df['Shipping.Cost'], df['ShippingC_Pred'])],
             'MSE':[mean_squared_error(df['Shipping.Cost'], df['ShippingC_Pred'])],
             'RMSE': [np.sqrt(mean_squared_error(df['Shipping.Cost'], df['ShippingC_Pred']))],
             'ME': [np.mean(df['Shipping.Cost']-df['ShippingC_Pred'])]}).rename(index={0:'Accuracy'})
#Purchase Intervals
#Data Mining Method to Locate Customers likely to churn who have long intrvals of ordering to send promotions

df_clean['Order.Date'] = pd.to_datetime(df_clean['Order.Date']) #initialize to datetime

def cust_view(bottom_n:int): #Input Parameter to view n customers likely to churn on basis of purchase interval
    cust_dic = {}
    for cust in df_clean['Customer.Name'].unique():
        cust_dic[cust]=np.mean([val for val in [x.days for x in df_clean[df_clean['Customer.Name'] == cust].\
     sort_values(by='Order.Date')['Order.Date'].diff(-1).abs().fillna(pd.Timedelta(days=0)).iloc[:-1]] if val!=0])
    
    cust_dic = dict(sorted(cust_dic.items(), key=lambda item: item[1], reverse=True)) #sort by time interval
    return pd.DataFrame(data = {'Customer_Name': cust_dic.keys(),
                     'Purchase_Interval': cust_dic.values()}).iloc[:bottom_n,:]

cust_view(100) #Input to view lowest 100 purchasing customer from interval calc
