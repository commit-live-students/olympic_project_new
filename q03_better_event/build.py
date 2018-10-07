# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
def fun(a,b):
    if(a>b):
        return 'Summer'
    if b<a:
        return 'Winter'
    else :
        return 'Both'
    
def q03_better_event(OlympicsDF):
    OlympicsDF['BetterEvent'] = list(map(lambda x,y : fun(x,y),OlympicsDF['Total_Summer'],OlympicsDF['Total_Winter']))
    return OlympicsDF
q03_better_event(OlympicsDF).BetterEvent.value_counts().max()
OlympicsDF[OlympicsDF['Total_Winter']== 0]['Total_Summer'].count




