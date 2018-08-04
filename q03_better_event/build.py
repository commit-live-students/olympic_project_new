# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
import pandas as pd

#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

# my solution

def q03_better_event(OlympicsDF):
    better_event = []
    for i in range(0,147):
        if OlympicsDF['Total_Summer'].iloc[i]>OlympicsDF['Total_Winter'].iloc[i]:
            better_event.append('Summer')
        elif OlympicsDF['Total_Summer'].iloc[i]<OlympicsDF['Total_Winter'].iloc[i]:
            better_event.append('Winter')
        else:
            better_event.append('Both')
    OlympicsDF['BetterEvent']=pd.Series(better_event)
    return OlympicsDF

#q03_better_event(OlympicsDF)







