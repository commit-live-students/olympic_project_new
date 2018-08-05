# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)
def q02_country_operations(x):
    x['Country Name']=x['Country']
    x['Country Name']=x.Country.str.split('(',expand=True)
    x['Country Name'] = x['Country Name'].map(lambda x: x.rstrip())

    return x
q02_country_operations(OlympicsDF)







