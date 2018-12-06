# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

#Purposely not passing paramters inside and hadcoding instead to avoid confusion while revising.
def q06_golden_winner(Dataset=OlympicsDF,list1=Top10Summer,list2=Top10Winter,list3=Top10):
    
    Summer = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)].loc[:,['Country_Name','Gold_Summer','Total_Summer']]
    Summer['Gold_Ratio']=Summer['Gold_Summer']/Summer['Total_Summer']
    Best_Country_Summer = Summer.sort_values(by='Gold_Ratio',ascending=False).iloc[0,0]

    Winter = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)].loc[:,['Country_Name','Gold_Winter','Total_Winter']]
    Winter['Gold_Ratio']=Winter['Gold_Winter']/Winter['Total_Winter']
    Best_Country_Winter = Winter.sort_values(by='Gold_Ratio',ascending=False).iloc[0,0]

    Total = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)].loc[:,['Country_Name','Gold_Total','Total']]
    Total['Gold_Ratio']=Total['Gold_Total']/Total['Total']
    Best_Country_Total = Total.sort_values(by='Gold_Ratio',ascending=False).iloc[0,0]

    return Best_Country_Summer,Best_Country_Winter,Best_Country_Total

#Call to the function-
q06_golden_winner()

