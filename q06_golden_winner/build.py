import pandas as pd
import numpy as np
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10):
    
    SummerOly = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    S_Ratio= list(SummerOly['Gold_Summer']/SummerOly['Total_Summer'])
    Summer_Country = SummerOly.iloc[np.argmax(S_Ratio), 16]
    
    WinterOly = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    W_Ratio= list(WinterOly['Gold_Winter']/WinterOly['Total_Winter'])
    Winter_Country = WinterOly.iloc[np.argmax(W_Ratio), 16]
    
    TotalOly = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]
    T_Ratio= list(TotalOly['Gold_Total']/TotalOly['Total'])
    Total_Country = TotalOly.iloc[np.argmax(T_Ratio), 16] 
    

    
    return Summer_Country, Winter_Country, Total_Country

q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10)



