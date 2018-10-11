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


def q05_top_10_plotting(df, l1, l2, l3):
    df1 = df[df['Country_Name'].isin(l1)]
    plt.bar(df1['Country_Name'],df1['Total'])
    
    df2 = df[df['Country_Name'].isin(l2)]
    plt.bar(df2['Country_Name'],df2['Total'])
    
    df3 = df[df['Country_Name'].isin(l3)]
    plt.bar(df3['Country_Name'],df3['Total'])
#     df4 = df[df['Country_Name'] in l4 ]
#     plt.bar(df4['Country_Name'],df4['total'])
    plt.show()

OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
# OlympicsDF['Country_Name']# in Top10Summer
# # Top10Summer


