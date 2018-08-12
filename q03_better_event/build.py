# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q03_better_event(OlympicsDF):
    total_summerlist = list(OlympicsDF['Total_Summer'])
    total_winter = list(OlympicsDF['Total_Winter'])
    newcolumndata =[conditioncheck(int(x),int(y)) for x,y in zip(total_summerlist,total_winter)]
    OlympicsDF['BetterEvent']=newcolumndata
   
    
    return OlympicsDF



def conditioncheck(x,y):
    if (x==y):
        return 'Both'
    elif (x>y):
        return 'Summer'
    else:
        return 'Winter'


q03_better_event(OlympicsDF)




