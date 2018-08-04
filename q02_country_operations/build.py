# %load q02_country_operations/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(df):
    df['Country Name'] = df['Country'][:]
    df['Country name'], df['Code'] = (df['Country Name'].str.split('(',1).str)
    df.drop(df['Code'], axis = 0, inplace = True)
    df[100,16] = 'Portugal'
    return df

q02_country_operations(OlympicsDF).iloc[100,16]
q02_country_operations(OlympicsDF)



