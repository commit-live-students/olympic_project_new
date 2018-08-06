# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
import pandas as pd
import numpy as np
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)  

def q04_find_top_10(df, Total_Summer, Total_Winter, Total):
     #
    df = df.iloc[:len(df)-1,:]
    Winter = list(df.sort_values('Total_Winter',ascending=False)['Country_Name'][0:10])
    Summer = list(df.sort_values('Total_Summer',ascending=False)['Country_Name'][0:10])
    sums = list(df.sort_values('Total',ascending=False)['Country_Name'][0:10])
    similar_data = set(Summer) & set(Winter) & set(sums)
    
    return (Summer, Winter,sums, similar_data)

q04_find_top_10(OlympicsDF, OlympicsDF['Total_Summer'], OlympicsDF['Total_Winter'], OlympicsDF['Total'])
#q04_find_top_10(q03_better_even)


