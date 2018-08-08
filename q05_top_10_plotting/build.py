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

def q05_top_10_plotting(df,p1,p2,p3):
    # summer value plotting 
    summer_value = df.loc[df['Country_Name'].isin(p1)]
    x_series = summer_value.index
    y_series = summer_value['Total']
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Summer')
    plt.plot(x_series,y_series)
    plt.xticks(summer_value.index,summer_value['Country_Name'])
    plt.show()
    
    #winter value plotting
    winter_value = df.loc[df['Country_Name'].isin(p2)]
    x_series = winter_value.index
    y_series = winter_value['Total']
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Winter')
    plt.plot(x_series,y_series)
    plt.xticks(winter_value.index,winter_value['Country_Name'])
    plt.show()
    
    #Top value plotting
    top_value = df.loc[df['Country_Name'].isin(p3)]
    x_series = top_value.index
    y_series = top_value['Total']
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10')
    plt.plot(x_series,y_series)
    plt.xticks(top_value.index,winter_value['Country_Name'])
    plt.show()
    
q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter, Top10)





