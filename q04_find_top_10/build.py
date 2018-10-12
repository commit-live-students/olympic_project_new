# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(OlympicsDF,col1,col2,col3):
    sorted_summer = OlympicsDF[['Country_Name',col1]].sort_values(col1,ascending=False)
    top_10_summer = (sorted_summer[1:].head(10))['Country_Name']

    sorted_winter = OlympicsDF[['Country_Name',col2]].sort_values(col2,ascending=False)
    top_10_winter = (sorted_winter[1:].head(10))['Country_Name']
    
    sorted_total = OlympicsDF[['Country_Name',col3]].sort_values(col3,ascending=False)
    top_10_total = (sorted_total[1:].head(10))['Country_Name']
    
    common = list(set(top_10_summer) & set(top_10_winter) & set(top_10_total))
    
    return list(top_10_summer),list(top_10_winter),list(top_10_total),common







