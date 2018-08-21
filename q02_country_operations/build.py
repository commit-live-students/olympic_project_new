# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(OlympicsDF):
    OlympicsDF['Country_Name'] = OlympicsDF['Country']
    OlympicsDF.iloc[100,16]='Portugal'
    return OlympicsDF

q02_country_operations(OlympicsDF)







