# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(OlympicsDF,summer,winter,total):
    OlympicsDF=OlympicsDF.iloc[:len(OlympicsDF)-1,:]
    top_ten_summer=[]
    top_ten_winter=[]
    top_ten_total=[]
    common=[]
    top_ten_winter = list(OlympicsDF.nlargest(10,'Total_Winter')['Country_Name'])
    top_ten_summer = list(OlympicsDF.nlargest(10,'Total_Summer')['Country_Name'])
    top_ten_total = list(OlympicsDF.nlargest(10,'Total')['Country_Name'])
    common = list(set(top_ten_total).intersection(set(top_ten_winter),set(top_ten_summer)))
    return top_ten_summer,top_ten_winter,top_ten_total,common




