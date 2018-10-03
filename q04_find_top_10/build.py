# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df=OlympicsDF,v1='Total_Summer',v2='Total_Winter',v3='Total'):
    top_10_summer=list(df.sort_values(v1,ascending=False)['Country_Name'][1:11])
    top_10_winter=list(df.sort_values(v2,ascending=False)['Country_Name'][1:11])
    top_10_overall=list(df.sort_values(v3,ascending=False)['Country_Name'][1:11])
    common_overall=list(set(top_10_summer).intersection(set(top_10_winter).intersection(set(top_10_overall)))) 
    return top_10_summer,top_10_winter,top_10_overall,common_overall





