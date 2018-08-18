# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
def q03_better_event(OlympicsDF):
    OlympicsDF['BetterEvent'] =''
    OlympicsDF['BetterEvent'][OlympicsDF['Total_Summer'] > OlympicsDF['Total_Winter']]= 'Summer'
    OlympicsDF['BetterEvent'][OlympicsDF['Total_Summer'] < OlympicsDF['Total_Winter']]= 'Winter'
    OlympicsDF['BetterEvent'][OlympicsDF['Total_Summer'] == OlympicsDF['Total_Winter']]= 'Both'
    return (OlympicsDF)

q03_better_event(OlympicsDF)



