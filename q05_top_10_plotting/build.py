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


def q05_top_10_plotting(df, Top10Summer, Top10Winter, Top10):
    df_Summer = df[df['Country_Name'].isin(Top10Summer)]
    df_Winter = df[df['Country_Name'].isin(Top10Winter)]
    df_Total  = df[df['Country_Name'].isin(Top10)]

    plt.bar(df_Summer['Country_Name'],df_Summer['Total_Summer'])
    plt.title = 'Top 10 Summer'
    plt.xlabel = 'Country Name'
    plt.ylabel = 'Total Medals'
    plt.show()

    plt.bar(df_Winter['Country_Name'],df_Summer['Total_Winter'])
    plt.title = 'Top 10 Winter'
    plt.xlabel = 'Country Name'
    plt.ylabel = 'Total Medals'
    plt.show()

    plt.bar(df_Total['Country_Name'],df_Summer['Total'])
    plt.title = 'Top 10'
    plt.xlabel = 'Country Name'
    plt.ylabel = 'Total Medals'
    plt.show()






