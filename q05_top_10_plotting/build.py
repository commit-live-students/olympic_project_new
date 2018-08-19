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
    df = df.iloc[:len(df)-1,:]
    Tota_Summer_Madels = df.sort_values('Total_Summer',ascending=False)[['Country_Name', 'Total_Summer']][0:10]
    plt.bar(Tota_Summer_Madels['Country_Name'], Tota_Summer_Madels['Total_Summer'])
    
    Total_Winter_Madels = df.sort_values('Total_Winter',ascending=False)[['Country_Name', 'Total_Winter']][0:10]
    plt.bar(Total_Winter_Madels['Country_Name'], Total_Winter_Madels['Total_Winter'])
    
    Total_Madels = df.sort_values('Total',ascending=False)[['Country_Name', 'Total']][0:10]
    plt.bar(Total_Madels['Country_Name'], Total_Madels['Total'])

q05_top_10_plotting(OlympicsDF, Top10Summer, Top10Winter, Top10)



