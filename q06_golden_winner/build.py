# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

import pandas as pd
def q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10):
    summer_data_frame = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)].sort_values(by=['Country_Name'], ascending = True)
    summer_data_frame['Gold/Total'] = summer_data_frame['Gold_Total']/summer_data_frame['Total']
    summer_country = summer_data_frame.nlargest(1,'Gold/Total')['Country_Name'].values[0]

    winter_data_frame = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)].sort_values(by=['Country_Name'], ascending = True)
    winter_data_frame['Gold/Total'] = winter_data_frame['Gold_Total']/winter_data_frame['Total']
    winter_country = winter_data_frame.nlargest(2,'Gold/Total').iloc[1,16]
    
    top_10 = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)].sort_values(by=['Country_Name'], ascending = True)
    top_10['Gold/Total'] = top_10['Gold_Total']/top_10['Total']
    top_country = top_10.nlargest(1,'Gold/Total')['Country_Name'].values[0]
    
    return summer_country, winter_country, top_country

q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10)

