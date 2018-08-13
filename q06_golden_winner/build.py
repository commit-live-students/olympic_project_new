# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10):
    Sum = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    Gold_Ratio_Sum = (Sum['Gold_Summer']/Sum['Total_Summer'])
    SUMC =Sum.get_value(Gold_Ratio_Sum.argmax(),'Country_Name')

    Win = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    Gold_Ratio_Win = (Win['Gold_Winter']/Win['Total_Winter'])
    WINC =Win.get_value(Gold_Ratio_Win.argmax(),'Country_Name')

    Top = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]
    Gold_Ratio_Top = (Top['Gold_Total']/Top['Total'])
    TOPC = Top.get_value(Gold_Ratio_Top.argmax(),'Country_Name')
    
    return SUMC, WINC, TOPC

q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10)





