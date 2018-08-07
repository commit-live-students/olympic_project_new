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

#Function definition 
def q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter, Top10):
    ''' Plotting top 10 countries for winter summer and total medals won'''
    
    #plot top 10 countries for summer
    medals_summer = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]['Total_Summer']
    countries_summer = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]['Country_Name']
    plt.bar(countries_summer,medals_summer)
    plt.xlabel('Country_Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Summer')
    plt.xticks(rotation=90)
    plt.show()

    #plot top 10 countries for winter
    medals_winter = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]['Total_Winter']
    countries_winter = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]['Country_Name']
    plt.bar(countries_winter,medals_winter)
    plt.xlabel('Country_Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10 Winter')
    plt.xticks(rotation=90)
    plt.show()

    #plot top 10 countries overall medals won
    medals_total = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]['Total']
    countries_total = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]['Country_Name']
    plt.bar(countries_total,medals_total)
    plt.xlabel('Country_Name')
    plt.ylabel('Total Medals')
    plt.title('Top 10')
    plt.xticks(rotation=90)
    plt.show()

#Function call for plotting
q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter, Top10)





