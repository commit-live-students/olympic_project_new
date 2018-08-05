# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)

def q02_country_operations(OlympicsDF = OlympicsDF):
    OlympicsDF['Country Name'] = OlympicsDF['Country'].str.replace(r'\xa0.*','')
    return OlympicsDF


#q02_country_operations()









