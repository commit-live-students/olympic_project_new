# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)

def q04_find_top_10(OlympicsDF,Total_Summer,Total_Winter,Total):
    sorted_1=OlympicsDF.sort_values('Total_Summer',ascending=False).iloc[1:11,-2].tolist()
    sorted_2=OlympicsDF.sort_values('Total_Winter',ascending=False).iloc[1:11,-2].tolist()
    sorted_3=OlympicsDF.sort_values('Total',ascending=False).iloc[1:11,-2].tolist()
    
    return sorted_1,sorted_2,sorted_3,list((set(sorted_1) & set(sorted_2)) & set(sorted_3))





