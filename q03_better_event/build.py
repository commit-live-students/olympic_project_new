# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
def f(row):
    if row['Total_Summer'] == row['Total_Winter']:
        val = 'Both'
    elif row['Total_Summer'] > row['Total_Winter']:
        val = 'Summer'
    elif row['Total_Summer'] < row['Total_Winter']:
        val = 'Winter'
    return val

def q03_better_event(OlympicsDF):
    OlympicsDF['BetterEvent'] = OlympicsDF.apply(f, axis=1)
    return OlympicsDF 




q03_better_event(OlympicsDF)


