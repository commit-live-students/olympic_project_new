# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10):
    OlympicsDF_total = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]
    OlympicsDF_total_summer = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    OlympicsDF_total_winter = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    OlympicsDF_total['Ratio_Total']=OlympicsDF_total['Gold_Total']/OlympicsDF_total['Total']
    OlympicsDF_total_winter['Ratio_Total']=OlympicsDF_total_winter['Gold_Winter']/OlympicsDF_total_winter['Total_Winter']
    OlympicsDF_total_summer['Ratio_Total']=OlympicsDF_total_summer['Gold_Summer']/OlympicsDF_total_summer['Total_Summer']
    total = list(OlympicsDF_total[OlympicsDF_total['Ratio_Total']==OlympicsDF_total['Ratio_Total'].max()]['Country_Name'])[0]
    total_winter = list(OlympicsDF_total_winter[OlympicsDF_total_winter['Ratio_Total']==OlympicsDF_total_winter['Ratio_Total'].max()]['Country_Name'])[0]
    total_summer = list(OlympicsDF_total_summer[OlympicsDF_total_summer['Ratio_Total']==OlympicsDF_total_summer['Ratio_Total'].max()]['Country_Name'])[0]
    return total_summer,total_winter,total

    
q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10)





