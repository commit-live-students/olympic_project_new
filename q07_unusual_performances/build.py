# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

df = OlympicsDF[:-1]
quantile_values = df['Total'].quantile([0.05, 0.95]).values

def q07_unusual_performances(df, lower_quantile_value, higher_quantile_value):
    lower_than_minimum_quantile = df.loc[df['Total'] <= lower_quantile_value]
    higher_than_maximum_quantile = df.loc[df['Total'] >= higher_quantile_value]
    return lower_than_minimum_quantile['Country_Name'].values, higher_than_maximum_quantile['Country_Name'].values
    

DF_Low, DF_High = q07_unusual_performances(OlympicsDF, quantile_values[0], quantile_values[1])





