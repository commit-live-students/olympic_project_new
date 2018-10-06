# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
data=q02_country_operations(OlympicsDF)

def q03_better_event(data):
    data['BetterEvent'] = 'Blank'
    data.loc[(data['Total_Summer'] > data['Total_Winter']),'BetterEvent']='Summer'
    data.loc[(data['Total_Summer'] < data['Total_Winter']),'BetterEvent']='Winter'
    data.loc[(data['Total_Summer'] == data['Total_Winter']),'BetterEvent']='Both'

    return data


