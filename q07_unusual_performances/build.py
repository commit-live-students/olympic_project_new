# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(df, lower_percentile, higher_percentile):
    df = df[:-1]
    quantile_values = df['Total'].quantile([lower_percentile, higher_percentile]).values
    lower_than_minimum_quantile = df.loc[df['Total'] <= quantile_values[0]]
    higher_than_maximum_quantile = df.loc[df['Total'] >= quantile_values[1]]
    return lower_than_minimum_quantile['Country_Name'], higher_than_maximum_quantile[['Country_Name', 'Total']]
    

# DF_Low, DF_High = q07_unusual_performances(OlympicsDF, 0.05, 0.95)





