# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'

def q03_better_event(df):
    OlympicsDF=q02_country_operations(df)
    OlympicsDF.loc[OlympicsDF['Total_Summer']<OlympicsDF['Total_Winter'],'BetterEvent'] = 'Winter'
    OlympicsDF.loc[OlympicsDF['Total_Summer']==OlympicsDF['Total_Winter'],'BetterEvent'] = 'Both'
    OlympicsDF.loc[OlympicsDF['Total_Summer']>OlympicsDF['Total_Winter'],'BetterEvent'] = 'Summer'
    return OlympicsDF

DataFrame=q01_rename_columns(path)    
q03_better_event(DataFrame)








