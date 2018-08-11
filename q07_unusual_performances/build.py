# %load q07_unusual_performances/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
high,low=0.95,0.05

def q07_unusual_performances(OlympicsDF,high,low):
    lower_bound=OlympicsDF.Total.quantile(.05)
    upper_bound=OlympicsDF.Total.quantile(.95)
    best_teams=OlympicsDF.loc[OlympicsDF['Total']>upper_bound,['Country_Name']].iloc[:-1]
    worst_teams=OlympicsDF.loc[OlympicsDF['Total']<=lower_bound,['Country_Name']]
    return  worst_teams.values, best_teams.values





