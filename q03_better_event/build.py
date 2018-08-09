# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def better_perf(x):
    if x[0] > x[1]:
        return 'Summer'
    elif x[0]< x[1] :
        return 'Winter'
    else:
        return 'Both'
    
def q03_better_event(OlympicsDF):
    OlympicsDF['BetterEvent'] =OlympicsDF[['Total_Summer','Total_Winter']].apply(better_perf, axis=1)
    
    return OlympicsDF










