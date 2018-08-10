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


def q05_top_10_plotting(OlympicsDF, Top10Summer, Top10Winter, Top10):
    df1 = OlympicsDF
    df1 = df1[df1.Country_Name.isin(Top10Summer) ==True][['Country_Name','Total_Summer']]
    ax1 = df1.plot.bar(x='Country_Name', y='Total_Summer',rot=0)
    df2 = OlympicsDF
    df2 = df2[df2.Country_Name.isin(Top10Winter) ==True][['Country_Name','Total_Winter']]
    ax2 = df2.plot.bar(x='Country_Name', y='Total_Winter',rot=0)
    df3 = OlympicsDF
    df3 = df3[df3.Country_Name.isin(Top10) ==True][['Country_Name','Total']]
    ax3 = df3.plot.bar(x='Country_Name', y='Total',rot=0)









