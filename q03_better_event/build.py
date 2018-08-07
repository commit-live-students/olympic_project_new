# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
def q03_better_event(OlympicsDf):
    OlympicsDF.loc[OlympicsDF['Total_Summer']==OlympicsDF['Total_Winter'],'BetterEvent'] = 'Both'
    OlympicsDF.loc[OlympicsDF['Total_Summer']<OlympicsDF['Total_Winter'],'BetterEvent'] = 'Winter'
    OlympicsDF.loc[OlympicsDF['Total_Summer']>OlympicsDF['Total_Winter'],'BetterEvent'] = 'Summer'
    return OlympicsDF.BetterEvent.value_counts().max()    
q03_better_event('OlympicsDF')






df.BetterEvent.value_counts().max()


