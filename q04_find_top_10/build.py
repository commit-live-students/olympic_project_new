# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(OlympicsDF,variable2,variable3,variable4):
       
    TSummer=OlympicsDF[:-1].sort_values(by=variable2, ascending=False).head(10)[['Country_Name']].index
    TWinter=OlympicsDF[:-1].sort_values(by=variable3, ascending=False).head(10)[['Country_Name']].index
    T10= OlympicsDF[:-1].sort_values(by=variable4, ascending=False).head(10)[['Country_Name']].index
    
    Top10Summer = list(OlympicsDF.iloc[TSummer]['Country_Name'])
    Top10Winter = list(OlympicsDF.iloc[TWinter]['Country_Name'])
    Top10 = list(OlympicsDF.iloc[T10]['Country_Name'])
    
    Common= [x for x in Top10Summer if x in Top10Winter and x in Top10]        
    return Top10Summer,Top10Winter, Top10, Common

q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')





