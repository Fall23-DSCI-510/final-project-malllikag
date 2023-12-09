[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Z1npak42)
Project Title: Geospatial Analysis of Global Superstore Sales 
Overview: The Global Superstore Sales Analysis project is a omprehensive exploration of sales and order data from a global superstore, aiming to derive meaningful insights for business optimization. Leveraging the Kaggle GLobal Superstore dataset, this project delves into patterns, trends, and regional variations within the sales landscape to inform strategic decision-making. 

Requirements Installation: 
Ensures that all necessary dependencies are installed by executing the following command: 
pip install -r requirements.txt

Getting the Data: 
Retrieve the raw data with the following command: 
python src/get_data.py 

Raw data files will be stored in the data/raw folder. 

Data Cleaning: 
Clean and preprocess the data using: 
python src/clean_data.py 

Cleaned and processed data will be stored in the 'data/processed' folder.

Running the Analysis: 
Execute the analysis code. 
python src/run_analysis.py 

This code performs various analyses on the processed data. 

Producing Visualizations: 
Generate visualizations with: 
python src/visualize results.py 

Visualizations will be saved in the 'results' folder. 

Project Structure: 
This project is organized as follows: 
- data/raw: Contains raw files downloaded and scraped from the web.
- data/processed: Contains structured files after data cleaning.
- results: Contains the final report and other project related files.
- src:
     - get_data.py: Downloads and stores data in the 'data/raw' folder.
     - clean_data.py: Cleans and transforms data, storing files in the 'data/processed' folder.
     - run_analysis.py: Code to analyze the data and answer project-specific questions.
     - visualize_results.py: Creates visualizations using libraries like Matplotlib.
 
  The notebook 'DSCI 510 Final.ipynb' located in the results folder can be run to achieve the above output.
