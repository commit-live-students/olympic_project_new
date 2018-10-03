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
    SOly=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    WOly=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    OOly=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]
    plt.subplot(2,2,1)
    plt.bar(SOly['Country_Name'],SOly['Total_Summer'],color='orange', label='Top 10 Summer')
    plt.xlabel('Countries')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Summer')

    plt.subplot(2,2,2)
    plt.bar(WOly['Country_Name'],WOly['Total_Winter'],color='cyan', label='Top 10 Winter')
    plt.xlabel('Countries')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Winter')

    plt.subplot(2,2,3)
    plt.bar(OOly['Country_Name'],OOly['Total'],color='green', label='Top 10 Overall')
    plt.xlabel('Countries')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Overall')
    plt.tight_layout(h_pad=1,w_pad=1,pad=1)
    plt.show()




