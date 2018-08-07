# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')


def q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10):
    
    SummerGoldRatio_temp = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    Top10Winter_temp = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    Top10_temp =  OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]
    
    SummerGoldRatio_temp['Gold_Ratio_Summer'] = (OlympicsDF['Gold_Summer'] / OlympicsDF['Total_Summer'])
    SummerGoldRatio_temp = SummerGoldRatio_temp[['Country_Name','Gold_Ratio_Summer']].sort_values(by='Gold_Ratio_Summer', ascending=False)
    SummerGoldRatio_temp = SummerGoldRatio_temp[0:1]
    SummerGoldRatio = ''.join(SummerGoldRatio_temp['Country_Name'])

    Top10Winter_temp['Gold_Ratio_Winter'] = (OlympicsDF['Gold_Winter'] / OlympicsDF['Total_Winter'])
    Top10Winter_temp = Top10Winter_temp[['Country_Name','Gold_Ratio_Winter']].sort_values(by='Gold_Ratio_Winter', ascending=False)
    Top10Winter_temp = Top10Winter_temp[0:1]
    WinterGoldRatio = ''.join(Top10Winter_temp['Country_Name'])

    Top10_temp['Gold_Ratio_Total'] = (OlympicsDF['Gold_Total'] / OlympicsDF['Total'])
    Top10_temp = Top10_temp[['Country_Name','Gold_Ratio_Total']].sort_values(by='Gold_Ratio_Total', ascending=False)
    Top10_temp = Top10_temp[0:1]
    TopGoldRatio = ''.join(Top10_temp['Country_Name'])
    
    return SummerGoldRatio, WinterGoldRatio, TopGoldRatio




