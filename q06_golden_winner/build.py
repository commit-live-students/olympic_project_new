# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10):
    OlympicsDF['GoldRatioSummer'] = OlympicsDF.loc[:,'Gold_Summer']/ OlympicsDF.loc[:,'Total_Summer']
    OlympicsDF['GoldRatioWinter'] = OlympicsDF.loc[:,'Gold_Winter']/ OlympicsDF.loc[:,'Total_Winter']
    OlympicsDF['GoldRatioTotal'] = OlympicsDF.loc[:,'Gold_Total']/ OlympicsDF.loc[:,'Total']
    
    top_10_summer_df = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    top_10_winter_df = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    top_10 = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]

    
    top_gold_summer = top_10_summer_df.sort_values('GoldRatioSummer',ascending=False).iloc[0,16]
    top_gold_winter = top_10_winter_df.sort_values('GoldRatioWinter',ascending=False).iloc[0,16]
    top_total = top_10.sort_values('GoldRatioTotal',ascending=False).iloc[0,16]
    
    return top_gold_summer,top_gold_winter,top_total








