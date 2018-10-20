# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
import pandas as pd
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)
OlympicsDF=OlympicsDF.drop([146])

def q04_find_top_10(df=OlympicsDF, str1 = 'Total_Summer', str2 = 'Total_Winter', str3 = 'Total'):
    top10_summer = list(OlympicsDF.nlargest(10, 'Total_Summer')['Country_Name'])
    top10_winter = list(OlympicsDF.nlargest(10, 'Total_Winter')['Country_Name'])
    top10_total = list(OlympicsDF.nlargest(10, 'Total')['Country_Name'])
    overall = list(set(top10_summer).intersection(set(top10_winter), set(top10_total)))
    
    return top10_summer, top10_winter, top10_total, overall

q04_find_top_10('Total_Summer', 'Total_Winter', 'Total')


    





