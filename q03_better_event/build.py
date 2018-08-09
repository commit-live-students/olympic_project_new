# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def get_better_event(item):
    print(item)

def q03_better_event(df):
    
    df['BetterEvent'] = np.where(df['Total_Summer'] > df['Total_Winter'], 'Summer', 
                                (np.where(df['Total_Summer'] == df['Total_Winter'], 'Both', 'Winter')))
    return df




