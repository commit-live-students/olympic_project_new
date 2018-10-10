# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q03_better_event(OlympicsDF):
    for i in range(len(OlympicsDF)):
        if OlympicsDF.loc[i,'Gold_Winter'] + OlympicsDF.loc[i,'Silver_Winter'] + OlympicsDF.loc[i,'Bronze_Winter'] > OlympicsDF.loc[i,'Gold_Summer'] + OlympicsDF.loc[i,'Silver_Summer'] + OlympicsDF.loc[i,'Bronze_Summer']:
            OlympicsDF.loc[i,'BetterEvent'] = 'Winter'
        elif OlympicsDF.loc[i,'Gold_Winter'] + OlympicsDF.loc[i,'Silver_Winter'] + OlympicsDF.loc[i,'Bronze_Winter'] == OlympicsDF.loc[i,'Gold_Summer'] + OlympicsDF.loc[i,'Silver_Summer'] + OlympicsDF.loc[i,'Bronze_Summer']:
            OlympicsDF.loc[i,'BetterEvent'] = 'Both'
        else:
            OlympicsDF.loc[i,'BetterEvent'] = 'Summer'
    return OlympicsDF








