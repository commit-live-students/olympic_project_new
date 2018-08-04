# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
import pandas as pd
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(df):
    df['Country Name']=df['Country'][:] 
    df['Country name']=(df['Country Name'].str.split('(',1).str)[0].str.strip
    
    return df
# q02_country_operations(OlympicsDF).iloc[100,16]
q02_country_operations(OlympicsDF).iloc[100,16]



#print(OlympicsDF.iloc[100,16])










