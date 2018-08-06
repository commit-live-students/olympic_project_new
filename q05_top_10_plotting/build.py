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

    list_Sum = OlympicsDF.nlargest(10,['Total_Summer'])
    y=list_Sum['Total_Summer']
    x=Top10Summer
    plt.bar(x,y)
    
    list_Win = OlympicsDF.nlargest(10,['Total_Winter'])
    a=list_Win['Total_Winter']
    b=Top10Winter
    plt.bar(a,b)
    
    list_T = OlympicsDF.nlargest(10,['Total'])
    y_1=list_T['Total']
    x_1=Top10
    plt.bar(x_1,y_1)

    return

q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter, Top10)




