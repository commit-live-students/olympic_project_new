# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)

def q02_country_operations(OlympicsDF):
    #OlympicsDF['Country Name'] = OlympicsDF['Country'].str.strip()
    OlympicsDF['Country Name'] = OlympicsDF['Country'].str.replace(r'[\(\[].*?[\)\]]','').str.replace(' ','').str.replace(u'\xa0','')
    OlympicsDF['Country Name']

    return OlympicsDF

q02_country_operations(OlympicsDF)
OlympicsDF['Country Name']





