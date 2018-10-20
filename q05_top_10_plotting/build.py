import matplotlib.pyplot as plt
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter,Top10):
    
    SummerOlympics = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]
    WinterOlympics = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
    FinalsOlympics = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]
    
    plt.subplot(2,2,1)
    plt.bar(SummerOlympics['Country_Name'], SummerOlympics['Total_Summer'], color= 'red', label= 'Top 10 Summer')
    plt.xlabel('Country')
    plt.ylabel('Total Medals')
    
    plt.subplot(2,2,2)
    plt.bar(WinterOlympics['Country_Name'], WinterOlympics['Total_Summer'], color= 'blue', label= 'Top 10 Winter')
    plt.xlabel('Country')
    plt.ylabel('Total Medals')

    plt.subplot(2,2,3)
    plt.bar(FinalsOlympics['Country_Name'], FinalsOlympics['Total_Summer'], color= 'green', label= 'Top 10')
    plt.xlabel('Country')
    plt.ylabel('Total Medals')
    
    plt.tight_layout()
    plt.show();
    
    





