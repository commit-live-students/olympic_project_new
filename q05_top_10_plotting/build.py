# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt

from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common = q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter,Top10):
    
    #For Summer
    top_10_summer = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)][['Country_Name','Total_Summer']]
    plt.bar(top_10_summer.Country_Name,top_10_summer.Total_Summer)
    plt.xticks(rotation=45)
    plt.show()
    
    #For Winter:
    top_10_winter = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)][['Country_Name','Total_Winter']]
    plt.bar(top_10_winter.Country_Name,top_10_winter.Total_Winter)
    plt.xticks(rotation=45)
    plt.show()
    
    top_10 = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)][['Country_Name','Total']]
    plt.bar(top_10.Country_Name,top_10.Total)
    plt.xticks(rotation=45)
    plt.show()





