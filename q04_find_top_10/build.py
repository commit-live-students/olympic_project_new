# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(variable1, variable2, variable3, variable4):
    df = variable1.drop(variable1.index[146])
    
    variable1 = list(df.sort_values(variable2, ascending=False).head(10)['Country_Name'])
    variable2 = list(df.sort_values(variable3, ascending=False).head(10)['Country_Name'])
    variable3 = list(df.sort_values(variable4, ascending=False).head(10)['Country_Name'])
    
    variable4 = []
    for element in variable1:
        if element in variable2 and element in variable3:
            variable4.append(element)
            
    return variable1, variable2, variable3, variable4
 
q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')


