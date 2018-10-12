# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF = (OlympicsDF[OlympicsDF['Country_Name'] != 'Totals' ])
df = OlympicsDF   

def q07_unusual_performances(df,low , high):
    a = df[df['Total'] <= low].Country_Name
    b = df[df['Total'] > high].Country_Name
    return a,b.iloc[:-1]

    

    
#q07_unusual_performances(df,low = 0.05, high = 0.95)


