# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
def func(x):
        
        if x['Total_Summer']>x['Total_Winter']:
            return 'Summer'
        elif x['Total_Summer']<x['Total_Winter']:
            return 'Winter'
        else :
            return 'Both'


def q03_better_event(df):
    
    df['BetterEvent']=df.apply(func,axis=1)
    return df






