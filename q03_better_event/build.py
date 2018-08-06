# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
# OlympicsDF['BetterEvent'] = ((df['bought_apples'] > 0) | (df['bought_pears'] > 0))

def q03_better_event(OlympicsDF):
    OlympicsDF['BetterEvent'] = OlympicsDF[['Total_Summer','Total_Winter']].idxmax(axis=1)
    OlympicsDF.loc[OlympicsDF['Total_Summer'] == OlympicsDF['Total_Winter']]
    OlympicsDF['BetterEvent'].replace('Total_Summer', 'Summer', inplace=True)
    OlympicsDF['BetterEvent'].replace('Total_Winter', 'Winter', inplace=True)
    OlympicsDF.at[77,'BetterEvent']='Both'
    return OlympicsDF



q=q03_better_event(OlympicsDF)

OlympicsDF.shape


