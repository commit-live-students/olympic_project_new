# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

OlympicsDF = OlympicsDF[:-1]
import numpy as np

low = 0.05
high = 0.95
def q07_unusual_performances(OlympicsDF, low, high):
    OlympicsDF = OlympicsDF.drop(OlympicsDF.index[23])
    
    low_value, high_value = OlympicsDF['Total'].quantile([0.05, 0.95])

    low_dataframe = OlympicsDF.iloc[np.where(OlympicsDF['Total'] <= low_value)]
    low_countries= low_dataframe['Country_Name']
    low_countries = low_countries.tolist()
    if('Totals' in low_countries):
        high_countries.remove('Totals')
    
    high_dataframe = OlympicsDF.iloc[np.where(OlympicsDF['Total'] > high_value)]
    high_countries = high_dataframe['Country_Name']
    
    high_countries = high_countries.tolist()
    if('Totals' in high_countries):
        high_countries.remove('Totals')
    
    return low_countries, high_countries

q07_unusual_performances(OlympicsDF, low, high)

