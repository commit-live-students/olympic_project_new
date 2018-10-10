# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(df):
    df['Country_Name'] = (df['Country'].str.split('(',1).str)[0].str.strip() 
    return df
#print(q02_country_operations(OlympicsDF))

#q02_country_operations(OlympicsDF)


