# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
import numpy as np
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10):
    SOly=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    WOly=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    OOly=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]
    Gold_Ratio_Summer=list(SOly['Gold_Summer']/SOly['Total_Summer'])
    summer_winner=SOly.iloc[np.argmax(Gold_Ratio_Summer),16]
    Gold_Ratio_Winter=list(WOly['Gold_Winter']/WOly['Total_Winter'])
    winter_winner=WOly.iloc[np.argmax(Gold_Ratio_Winter),16]
    Gold_Ratio_Total=list(OOly['Gold_Total']/OOly['Total'])
    total_winner=OOly.iloc[np.argmax(Gold_Ratio_Total),16]
    return summer_winner, winter_winner, total_winner
q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10)





