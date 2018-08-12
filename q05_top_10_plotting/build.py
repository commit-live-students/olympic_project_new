# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt
import numpy as np
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
# Top10Summer,Top10Winter, Top10=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q05_top_10_plotting(df,Top10Summer,Top10Winter, Top10):
    
    summer_df = df.loc[df['Country_Name'].isin(Top10Summer), ['Country_Name', 'Total']]
    summer_df = summer_df.groupby('Country_Name').sum()
    
    winter_df = df.loc[df['Country_Name'].isin(Top10Winter), ['Country_Name', 'Total']]
    winter_df = winter_df.groupby('Country_Name').sum()
    
    total_df = df.loc[df['Country_Name'].isin(Top10), ['Country_Name', 'Total']]
    total_df = total_df.groupby('Country_Name').sum()
    
    bar_summer = plt.bar(summer_df.index, summer_df['Total'])
    bar_winter = plt.bar(winter_df.index, winter_df['Total'])
    bar_total = plt.bar(total_df.index, total_df['Total'])

    return bar_summer, bar_winter, bar_total

q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter, Top10)





