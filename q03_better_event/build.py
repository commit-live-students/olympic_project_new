# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q03_better_event(OlympicsDF):
    
    OlympicsDF['BetterEvent'] = np.empty
    for i in range(len(OlympicsDF)):
        if OlympicsDF.iloc[i, 5] > OlympicsDF.iloc[i, 10]:
            #summer 
            OlympicsDF['BetterEvent'][i] = 'Summer'
        if OlympicsDF.iloc[i, 5] < OlympicsDF.iloc[i, 10]:
            #winter
            OlympicsDF['BetterEvent'][i] = 'Winter'
        if OlympicsDF.iloc[i, 5] == OlympicsDF.iloc[i, 10]:
            #both
            OlympicsDF['BetterEvent'][i] = 'Both'

    return OlympicsDF


df = q03_better_event(OlympicsDF)
df.BetterEvent.value_counts().max()
df.shape
df.BetterEvent.value_counts().max()



