# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
import pandas as pd
import numpy as np
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df ,Sum,Win,Total):
    df=df[:146]
    list_Sum, list_Win, list_T, Common = [] , [] ,[] , []
    list_Sum = df.nlargest(10,Sum)
  
    list_Win = df.nlargest(10,Win)
    list_T = df.nlargest(10,Total)
    com = list(set(list_Sum['Country_Name']).intersection(list_Win['Country_Name'],list_T['Country_Name']))
    
    #Common_L =set(Common).intersection(list_T)
    
    return (list_Sum['Country_Name'].reset_index(drop=True)),(list_Win['Country_Name'].reset_index(drop=True)),(list_T['Country_Name'].reset_index(drop=True)),com
    
q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')








