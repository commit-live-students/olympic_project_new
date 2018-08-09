# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
OlympicsDF.drop(OlympicsDF.tail(1).index,inplace=True) 

def q04_find_top_10(variable1,variable2,variable3,variable4):
    variable1 = OlympicsDF.sort_values(by='Total_Summer',ascending=False)
    variable1 = variable1['Country_Name'].head(10).values.tolist()
    variable2 = OlympicsDF.sort_values(by='Total_Winter',ascending=False)
    variable2 = variable2['Country_Name'].head(10).values.tolist()
    variable3 = OlympicsDF.sort_values(by='Total',ascending=False)
    variable3 = variable3['Country_Name'].head(10).values.tolist()
    variable4 = set(variable1) & set(variable2) & set(variable3)
    variable4 = list(variable4)
    return (variable1,variable2,variable3,variable4)
q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')




