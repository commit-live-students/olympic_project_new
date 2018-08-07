# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter,Top10):
    m = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]['Total']
    plt.plot(Top10Summer,m)
    plt.show()
    a = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]['Total']
    plt.plot(Top10Winter,a)
    plt.show()
    k = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]['Total']
    plt.plot(Top10Summer,k)
    plt.show()


q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter,Top10)






