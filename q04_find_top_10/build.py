# %load q04_find_top_10/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(Olympicsdf,Total_Summer,Total_Winter,Total):
    OlympicsDF = Olympicsdf[0:-1]
    Top10summer = OlympicsDF.sort_values(['Total_Summer'], ascending = False).head(10)
    Top10winter = OlympicsDF.sort_values(['Total_Winter'], ascending = False).head(10)
    Top_10= OlympicsDF.sort_values(['Total'], ascending = False).head(10)
    Common = pd.merge(pd.merge(Top10summer,Top10winter, on = 'Country_Name'),Top_10,on = 'Country_Name')
    return list(Top10summer['Country_Name']),list(Top10winter['Country_Name']),list(Top_10['Country_Name']),list(Common['Country_Name'])

q04_find_top_10(OlympicsDF,OlympicsDF['Total_Summer'],OlympicsDF['Total_Winter'],OlympicsDF['Total'])





