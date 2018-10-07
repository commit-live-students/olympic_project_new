# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
df=q03_better_event(OlympicsDF) 
# df.drop(df.tail(1).index,inplace=True)
def q04_find_top_10(df = df, col1 = 'Total_Summer', col2 ='Total_Winter',col3 = 'Total'):
   
    SummerList = (df.sort_values(col1,ascending = False).reset_index(drop =True))[1:11]
    variable2 = (df.sort_values(col2,ascending = False).reset_index(drop =True))[1:11]
    variable3 = (df.sort_values(col3,ascending = False).reset_index(drop =True))[1:11]
    temp = list(set(list(SummerList['Country_Name'])).intersection(list(variable2['Country_Name'])))
    variable4 = list(set(temp).intersection(list(variable3['Country_Name'])))
    #variable4 = list(['Germany', 'Sweden', 'United States', 'Soviet Union'])
    return list(SummerList['Country_Name']), list(variable2['Country_Name']), list(variable3['Country_Name']),variable4



