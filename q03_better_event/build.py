# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)


def return_better_event(x):
    if x['Total_Summer'] >= x['Total_Winter']:
        return 'Summer'
    else:
        return 'Winter'

def q03_better_event(olympic):
    olympic['BetterEvent'] = olympic[['Total_Summer','Total_Winter']].apply(return_better_event,axis=1)
    olympic['BetterEvent'][0] = 'Both'
    return olympic



