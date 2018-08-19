# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
import pandas as pd
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q03_better_event(OlympicsDF=OlympicsDF):
    BetterEvent_col = []
    for i, j in zip(OlympicsDF['Total_Summer'], OlympicsDF['Total_Winter']): 
        if i > j:
            BetterEvent_col.append('Summer')
        elif i < j:
            BetterEvent_col.append('Winter')
        else:
            BetterEvent_col.append('Both')

    OlympicsDF['BetterEvent'] = BetterEvent_col
    return OlympicsDF



