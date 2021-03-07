# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
def q04_find_top_10(OlympicsDF,Total_Summer,Total_Winter,Total):
    OlympicsDF.drop(OlympicsDF.tail(1).index,inplace=True)
    list1=list(OlympicsDF.nlargest(10,'Total_Summer')['Country_Name'].values)
    list2=list(OlympicsDF.nlargest(10,'Total_Winter')['Country_Name'].values)
    list3=list(OlympicsDF.nlargest(10,'Total')['Country_Name'].values)
    list4=list(set(list1).intersection(list2).intersection(list3))
    return list1,list2,list3,list4
OlympicsDF


