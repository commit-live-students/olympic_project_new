# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'   
import pandas as pd
def q04_find_top_10(DF1,Total_Summer,Total_Winter,Total):
    OlympicsDF = DF1[0:-1]
    SummerList = OlympicsDF.sort_values(['Total_Summer'], ascending = False).head(10)
    WinterList = OlympicsDF.sort_values(['Total_Winter'], ascending = False).head(10)
    Top= OlympicsDF.sort_values(['Total'], ascending = False).head(10)
    CommonElements = pd.merge(pd.merge(SummerList,WinterList, on = 'Country_Name'),Top,on = 'Country_Name')
    return list(SummerList['Country_Name']),list(WinterList['Country_Name']),list(Top['Country_Name']),list(CommonElements['Country_Name'])

DF=q01_rename_columns(path)    
DF=q02_country_operations(DF)
DF=q03_better_event(DF)
q04_find_top_10(DF,DF['Total_Summer'],DF['Total_Winter'],DF['Total'])



['United States',
 'Soviet Union',
 'Great Britain',
 'Germany',
 'France',
 'Italy',
 'Sweden',
 'China',
 'East Germany',
 'Russia']


