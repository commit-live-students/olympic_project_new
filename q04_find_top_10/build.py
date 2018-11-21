# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(OlympicsDF=OlympicsDF,col1='Total_Summer',col2='Total_Winter',col3='Total'):
    df1=OlympicsDF.drop(146).nlargest(10,col1)
    l1=list(df1['Country_Name'])
    df2=OlympicsDF.drop(146).nlargest(10,col2)
    l2=list(df2['Country_Name'])
    df3=OlympicsDF.drop(146).nlargest(10,col3)
    l3=list(df3['Country_Name'])
    l4=[i for i in l1 if i in l2 and l3]
    return l1,l2,l3,l4
df1=OlympicsDF.drop(146).nlargest(10,'Total_Summer')
l1=list(df1['Country_Name'])
df2=OlympicsDF.drop(146).nlargest(10,'Total_Winter')
l2=list(df2['Country_Name'])
df3=OlympicsDF.drop(146).nlargest(10,'Total')
l3=list(df3['Country_Name'])
l1 in l2
[i for i in l1 if i in l2 and l3]
q04_find_top_10()


