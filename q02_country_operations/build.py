# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(OlympicsDF):
    OlympicsDF['Country_Name'] = OlympicsDF['Country'].apply(str).apply(change_name)
    OlympicsDF.iloc[100,16] = 'Portugal'
    return OlympicsDF

def change_name(name):
    modified_name = ''
    for x in range(0,len(name)):
        if name[x] == '\xa0':
            modified_name = name[0:x]
    return modified_name


