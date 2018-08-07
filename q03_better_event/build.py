# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q03_better_event(OlympicsDF):
    a = OlympicsDF['Total_Summer']
    b = OlympicsDF['Total_Winter']

    BetterEvent = []
    for x,y in zip(a,b):
        if x > y:
            BetterEvent.append('Summer')
        elif y > x:
            BetterEvent.append('Winter')
        else:
            BetterEvent.append('Both')
        
    OlympicsDF['BetterEvent'] = BetterEvent            
    return OlympicsDF    






