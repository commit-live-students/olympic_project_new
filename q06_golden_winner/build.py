# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
import pandas as pd
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10):
    O=OlympicsDF.set_index('Country_Name')
    O=O.loc[Top10,['Total','Gold_Summer','Total_Summer','Gold_Winter','Total_Winter','Gold_Total']]
    O['ratio']=O['Gold_Total']/O['Total']
    O['sratio']=O['Gold_Summer']/O['Total_Summer']
    O['wratio']=O['Gold_Winter']/O['Total_Winter']
    return O.sratio.idxmax(), O.wratio.idxmax(), O.ratio.idxmax()
q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10)




