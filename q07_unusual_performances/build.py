# %load q07_unusual_performances/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

low=0.05
high=0.95
quant_df = OlympicsDF['Total'].quantile([low, high])
low1 = quant_df.loc[low] 
high1 = quant_df.loc[high]

def q07_unusual_performances(OlympicsDF, low1, high1):
    worst_teams = list(OlympicsDF[OlympicsDF['Total'] <= low1]['Country_Name'])
    better_teams = list(OlympicsDF[(OlympicsDF['Total'] > high1) & (OlympicsDF['Country_Name'] != 'Totals')]['Country_Name'])
    return worst_teams,better_teams
q07_unusual_performances(OlympicsDF,low1,high1)




