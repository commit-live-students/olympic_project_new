# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)

def q02_country_operations(OlympicsDF):
    '''Approach 1: Creating a duplicate dataFrame and adding a new column to it
    Using the 'apply' method to apply lambda function to all elements of the 'Country'
    column. Space in python is represented as: '\xa0'. Split method return a list and hence we
    are using [0] to retrieve the first element of the list.
    '''
    newDF = OlympicsDF
    newDF['Country_Name'] = newDF['Country'].apply(lambda x: x.split('\xa0')[0])
    return newDF

q02_country_operations(OlympicsDF)


