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

def q05_top_10_plotting(q04_find_top_10,Top10Summer,Top10Winter, Top10):
    df=OlympicsDF
    a=df[df['Country_Name'].isin(Top10Summer)]#sort df according to values in Top10Smmer list
    b=plt.bar(a['Country_Name'],a['Total'])
    c=df[df['Country_Name'].isin(Top10Winter)]
    d=plt.bar(c['Country_Name'],c['Total'])
    e=df[df['Country_Name'].isin(Top10)]
    f=plt.bar(e['Country_Name'],e['Total'])
    return b,d,f
    
     





c=q05_top_10_plotting(q04_find_top_10,Top10Summer,Top10Winter, Top10)
c


