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


def q05_top_10_plotting(olympic , top_summer_countries, top_winter_countries , top_countries ):
    
    top_df = olympic[olympic['Country_Name'].isin(top_countries)]
    xseries = list(top_df['Country_Name'])
    yseries = list(top_df['Total'])
    plt.title('top countries combined medals graph')
    plt.ylabel('no of medals')
    plt.xlabel('countries')
    plt.xticks(rotation = 90)
    plt.bar(xseries,yseries)
    plt.show()


    top_summer_df = olympic[olympic['Country_Name'].isin(top_summer_countries)]
    x1series = list(top_summer_df['Country_Name'])
    y1series = list(top_summer_df['Total_Summer'])
    plt.title('top summer countries combined medals graph')
    plt.ylabel('no of medals')
    plt.xlabel('countries')
    plt.xticks(rotation = 90)
    plt.bar(x1series,y1series)
    plt.show()

    top_winter_df = olympic[olympic['Country_Name'].isin(top_winter_countries)]
    x2series = list(top_winter_df['Country_Name'])
    y2series = list(top_winter_df['Total_Winter'])
    plt.title('top winter countries combined medals graph')
    plt.ylabel('no of medals')
    plt.xlabel('countries')
    plt.xticks(rotation = 90)
    plt.bar(x2series,y2series)
    plt.show()



