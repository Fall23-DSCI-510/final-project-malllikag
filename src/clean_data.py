import pandas as pd 

def clean_data(dataframe):
  dataframe = dataframe.dropna(axis=1, how='all')
  dataframe = dataframe.dropna(subset=dataframe.columns[dataframe.isnull().any()])
  return dataframe

def save_cleaned_data(cleaned_dataframe, output_filename):
  cleaned_dataframe.to_csv(output_filename, index=False)

def clean_csv_file(input_filename, output_filename)
  data=pd.read_csv(input_filename)
  cleaned_data=clean_data(data)
  save_cleaned_data(cleaned_data, output_filename)

clean_csv_file('Regional_LACrimes_Yearly.csv', 'data/processed/cleaned_la_crimes.csv')
clean_csv_file('ca_zip_pop.csv', 'data/processed/cleaned_ca_zip_pop.csv')
