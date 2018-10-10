# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q03_better_event(OlympicsDF):
    
    OlympicsDF['BetterEvent'] = OlympicsDF.apply(test, axis= 1)
    
    return OlympicsDF


def test(s):
    if s['Total_Summer'] > s['Total_Winter']:
        return 'Summer'
    elif s['Total_Summer'] < s['Total_Winter']:
        return 'Winter'
    else:
        return 'Both'











