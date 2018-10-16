# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

#OlympicsDF['BetterEvent']

# def f(df):
#     if df.iloc[:,1] == df.iloc[:,6]:
#         val = 'Both'
#     elif df.iloc[:,1] > df.iloc[:,6]:
#         val = 'Summer'
#     else df.iloc[:,1] == df.iloc[:,6]:
#         val = 'Winter'
#     return val

def q03_better_event(OlympicsDF):
    OlympicsDF.loc[OlympicsDF.iloc[:,5] == OlympicsDF.iloc[:,10], 'BetterEvent'] = 'Both'
    OlympicsDF.loc[OlympicsDF.iloc[:,5] > OlympicsDF.iloc[:,10], 'BetterEvent'] = 'Summer'
    OlympicsDF.loc[OlympicsDF.iloc[:,5] < OlympicsDF.iloc[:,10], 'BetterEvent'] = 'Winter'
    return OlympicsDF
    
q03_better_event(OlympicsDF)['BetterEvent']

OlympicsDF.head()




