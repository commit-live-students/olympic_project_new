# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)
def q02_country_operations(dataframe):    
    OlympicsDF['Country Name'] = OlympicsDF['Country'].str.split('(').str[0].str.strip()
    OlympicsDF['Country Name']
    return OlympicsDF
   # return OlympicsDF['Country'].str.split('(').str[0].str.strip()

a = q02_country_operations(OlympicsDF)

a

a[a['Country Name']=='Portugal']
OlympicsDF['Country Name'] = OlympicsDF['Country'].str.split('(').str[0].str.rstrip('\W')
#OlympicsDF[OlympicsDF['Country Name'].str.contains('Portugal')]['Country Name'].str.rstrip('\W')
OlympicsDF[OlympicsDF['Country Name'] == 'Portugal']



