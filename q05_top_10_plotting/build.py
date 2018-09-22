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
    Top10Summer = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10Summer)].loc[:,['Country_Name', 'Total']]
    Top10Summer.plot(x='Country_Name', y='Total',kind='bar')
    
    Top10Winter = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10Winter)].loc[:,['Country_Name', 'Total']]
    Top10Winter.plot(x='Country_Name', y='Total',kind='bar')
    
    Top10 = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10)].loc[:,['Country_Name', 'Total']]
    Top10.plot(x='Country_Name', y='Total',kind='bar')
    plt.show()
    
q05_top_10_plotting(OlympicsDF,Top10Summer,Top10Winter, Top10)






