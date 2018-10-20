# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    


def q04_find_top_10(OlympicsDF, Total_Summer, Total_Winter, Total):
    
    total_summer = OlympicsDF.sort_values(by=Total_Summer, ascending=False)['Country_Name'].iloc[1:11]
    total_winter = OlympicsDF.sort_values(by=Total_Winter, ascending=False)['Country_Name'].iloc[1:11]
    total = OlympicsDF.sort_values(by=Total, ascending=False)['Country_Name'].iloc[1:11]
    common = set(total_summer) & set(total_winter) & set(total)
    return total_summer, total_winter, total, common
    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
Top10Winter
OlympicsDF.sort_values(by='Total_Winter', ascending=False)[['Total_Winter', 'Country_Name']].iloc[1:11]






