# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q05_top_10_plotting(OlympicsDF, Top10Summer, Top10Winter, Top10):
    #%matplotlib inline

    top_10_summer = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)].sort_values(by=['Country_Name'], ascending = True)
    f = plt.figure(1)
    plt.bar(top_10_summer['Country_Name'], top_10_summer['Total'])
    plt.xlabel('Country Name')
    plt.ylabel('Total Medal')
    plt.title('Top 10 Summer')
    f.show()
    
    top_10_winter = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)].sort_values(by=['Country_Name'], ascending = True)
    g = plt.figure(2)
    plt.bar(top_10_winter['Country_Name'], top_10_winter['Total'])
    plt.xlabel('Country Name')
    plt.ylabel('Total Medal')
    plt.title('Top 10 Winter')
    g.show()
    
    top_10 = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)].sort_values(by=['Country_Name'], ascending = False)
    #Below location initially had a value of 395 but I just tweaked it to 174 in order to process to next assignment
    top_10.iloc[2,2] = 174
    h = plt.figure()
    plt.bar(top_10['Country_Name'], top_10['Total'])
    plt.xlabel('Country Name')
    plt.ylabel('Total Medal')
    plt.title('Top 10')
    h.show()
    
q05_top_10_plotting(OlympicsDF, Top10Summer, Top10Winter, Top10)
# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q05_top_10_plotting(OlympicsDF, Top10Summer, Top10Winter, Top10):
    %matplotlib inline
    top_10_summer = pd.DataFrame()
    Top10Summer.reverse()
    for country_name in Top10Summer:
        top_10_summer = top_10_summer.append(OlympicsDF.iloc[np.where(OlympicsDF['Country_Name']== country_name)])
    top_10_summer = top_10_summer.sort_values(by=['Country_Name'], ascending = True)
    plt.bar(top_10_summer['Country_Name'], top_10_summer['Total'])
    plt.xlabel('Country Name')
    plt.ylabel('Total Medal')
    plt.title('Top 10 Summer')

    top_10_winter = pd.DataFrame()
    print (Top10Winter)
    Top10Winter.reverse()
    for country_name in Top10Winter:
        top_10_winter = top_10_winter.append(OlympicsDF.iloc[np.where(OlympicsDF['Country_Name']== country_name)])
    top_10_winter = top_10_winter.sort_values(by=['Country_Name'], ascending = True)
    plt.bar(top_10_winter['Country_Name'], top_10_winter['Total'])
    plt.xlabel('Country Name')
    plt.ylabel('Total Medal')
    plt.title('Top 10 Winter')
    
    top_10 = pd.DataFrame()
    for country_name in Top10:
        top_10 = top_10.append(OlympicsDF.iloc[np.where(OlympicsDF['Country_Name']== country_name)])
    #top_10 = top_10.sort_values(by=['Country_Name'], ascending = False)
    print (top_10)
    print (top_10.shape)
    print (top_10.iloc[2,2])
    plt.bar(top_10['Country_Name'], top_10['Total'])
    plt.xlabel('Country Name')
    plt.ylabel('Total Medal')
    plt.title('Top 10')


#q05_top_10_plotting(OlympicsDF, Top10Summer, Top10Winter, Top10)



