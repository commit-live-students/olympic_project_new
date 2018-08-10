# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(var1,var2,var3,var4):
    df = var1[:146]
    df1 = df.sort_values(var2, ascending=False)
    l1 = list(df1.head(10)['Country_Name'])
    
    df2 = df.sort_values(var3, ascending=False)
    l2 = list(df2.head(10)['Country_Name'])
    
    df3 = df.sort_values(var4, ascending=False)
    l3 = list(df3.head(10)['Country_Name'])
#     df1 = df.sort_values('Total_Summer', ascending=False)
#     l1 = list(df1.head(10)['Country_Name'])
    l4=list(set(l1) & set(l2) & set(l3))
    return l1,l2,l3,l4








