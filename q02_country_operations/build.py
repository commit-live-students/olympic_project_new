# %load q02_country_operations/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(df):
    df['Country name'] = (df['Country'].str.split('(',1).str)[0].str.strip()
    #df.drop(labels=['Code'], axis=1, inplace=True)
    #df.iloc[100,16] = 'Portugal'
    return df

q02_country_operations(OlympicsDF).shape



