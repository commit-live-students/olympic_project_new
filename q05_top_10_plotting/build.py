# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt
import pandas as pd
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter,Top10):
    sl,wl,tl=[],[],[]
    for i in range(0,10):
        s=OlympicsDF.Total_Summer[OlympicsDF['Total_Summer'].notnull()&(OlympicsDF['Country_Name']==Top10Summer[i])]
        sl+=list(s)
        w=OlympicsDF.Total_Winter[OlympicsDF['Total_Winter'].notnull()&(OlympicsDF['Country_Name']==Top10Winter[i])]
        wl+=list(w)
        t=OlympicsDF.Total_Winter[OlympicsDF['Total'].notnull()&(OlympicsDF['Country_Name']==Top10[i])]
        tl+=list(t)   
    plt.bar(Top10Summer,sl)
    plt.xlabel('country')
    plt.ylabel('medal count')
    plt.title('Top10Summer')
    plt.xticks(Top10Summer,rotation=90)
    plt.show()
    plt.bar(Top10Winter,wl)
    plt.xlabel('country')
    plt.ylabel('medal count')
    plt.title('Top10Winter')
    plt.xticks(Top10Winter,rotation=90)
    plt.show()
    plt.bar(Top10,tl)
    plt.xlabel('country')
    plt.ylabel('medal count')
    plt.title('Top10')
    plt.xticks(Top10,rotation=90)
    plt.show()
q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter,Top10)        
        






