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
    
    
    
    plt.bar(Top10Summer,list(OlympicsDF.nlargest(10,'Total_Summer')['Total_Summer'].values))
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Summer')
    plt.bar(Top10Winter,list(OlympicsDF.nlargest(10,'Total_Winter')['Total_Winter'].values))
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Winter')
    plt.bar(Top10,list(OlympicsDF.nlargest(10,'Total')['Total'].values))
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10')
    plt.show()


Top10Summer
list(OlympicsDF.nlargest(10,'Total_Summer')['Total_Summer'].values)


