# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

#Function definition
def q03_better_event(OlympicsDF):
    i=0
    #Create a new blank column
    OlympicsDF['BetterEvent'] = pd.Series([])

    #Initiate a loop to compare each row value in totl winter summer and then set value 
    while i < OlympicsDF['Total_Summer'].size:
        if OlympicsDF['Total_Summer'][i] > OlympicsDF['Total_Winter'][i]:
            OlympicsDF['BetterEvent'][i] = 'Summer'
        elif OlympicsDF['Total_Summer'][i] < OlympicsDF['Total_Winter'][i]:
            OlympicsDF['BetterEvent'][i] = 'Winter'
        else:
            OlympicsDF['BetterEvent'][i] = 'Both'
        i=i+1
    return OlympicsDF
    
#Function call    
q03_better_event(OlympicsDF)
OlympicsDF['BetterEvent'].value_counts().max()
OlympicsDF.shape
OlympicsDF


