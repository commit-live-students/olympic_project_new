# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
def q02_country_operations():
    OlympicsDF=q01_rename_columns(path)    
    OlympicsDF['Country_Name']=OlympicsDF['Country']
    OlympicsDF['Country_Name']=OlympicsDF['Country_Name'].str.lstrip()
    return(OlympicsDF)


