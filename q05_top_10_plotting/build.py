# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt
import pandas as pd
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common = q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')


def q05_top_10_plotting(Dataset,col1=Top10Summer,col2=Top10Winter,col3=Top10):

    Dataset[Dataset['Country_Name'].isin(col1)].plot(x='Country_Name',y='Total_Summer',kind='bar')
    plt.title('Top 10 Summer')
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')

    Dataset[Dataset['Country_Name'].isin(col2)].plot(x='Country_Name',y='Total_Winter',kind='bar')
    plt.title('Top 10 Winter')
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')

    Dataset[Dataset['Country_Name'].isin(col3)].plot(x='Country_Name',y='Total',kind='bar')
    plt.title('Top 10')
    plt.xlabel('Country Name')
    plt.ylabel('Total Medals')
    plt.show() 

#Call to the function
q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter,Top10)

