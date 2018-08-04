# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
import pandas

#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(df):
    df['Country Name'] = df['Country'][0:]
    df['Country Name'] = (df['Country Name'].str.split('(',1).str)[0].str.strip()
    
    return df

q02_country_operations(OlympicsDF)



