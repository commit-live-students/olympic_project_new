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

def q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter, Top10):
    dftopsummer =OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]   
    dfTop10Winter =OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]   
    dfCommon =OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]   

    plt.bar(dftopsummer['Country_Name'], dftopsummer['Total'],align='center', alpha=0.5)
    plt.ylabel('Total Medal')
    plt.xlabel('Country Name')
    plt.title('Top 10 Summer') 
    plt.show()

    plt.bar(dfTop10Winter['Country_Name'], dfTop10Winter['Total'],align='center', alpha=0.5)
    plt.ylabel('Total Medal')
    plt.xlabel('Country Name')
    plt.title('Top 10 Winter') 
    plt.show()
    
    plt.bar(dfCommon['Country_Name'], dfCommon['Total'],align='center', alpha=0.5)
    plt.ylabel('Total Medal')
    plt.xlabel('Country Name')
    plt.title('Top 10 ') 
    plt.show()




