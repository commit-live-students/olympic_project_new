# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

low, high = OlympicsDF['Total'].quantile([0.05,0.95])

def q07_unusual_performances(df1,l,h):
    df1 = df1.iloc[:-1,:]
    df2 = df1['Total'] <= l
    df3 = df1['Total'] >= h
    return df1[df2]['Country_Name'],df1[df3]['Country_Name']



