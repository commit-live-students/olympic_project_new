# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
import re
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)   

def regular_exp(values):
      return values.split('(')[0].strip()

def q02_country_operations(df):
    tf = df['Country'].apply(regular_exp)
    df['Country_Name'] = tf
    return df
    






