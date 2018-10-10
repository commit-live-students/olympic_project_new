# %load q05_top_10_plotting/build.py
# default imports
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')



    
def q05_top_10_plotting(variable1, variable2, variable3, variable4):
    
    helping(variable1, variable2, 'summer')
    helping(variable1, variable3,'winter')
    helping(variable1, variable4, 'winter + summer')
    
def helping(df, country_list, time):
    co = []
    for element in country_list:
        co = co + (list(df[df['Country_Name'] == element]['Total_Summer']))
  
    plt.figure()
    co = np.array(co)
    plt.bar(country_list, co)
    plt.xticks(rotation = 50)
    plt.xlabel('Country Name')
    plt.ylabel('Total '+time+ ' medal')
    plt.show()
    


q05_top_10_plotting(OlympicsDF, Top10Summer,Top10Winter, Top10)
len(Top10Summer)


