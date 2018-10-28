# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
import pandas as pd

#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)

def q02_country_operations(dataframe=OlympicsDF):
    dataframe['Country_Name'] = dataframe.Country.str.split('(').str[0].str.strip()
    
    #dataframe.Country.str.split('(') - splits the column into 2 columns viz. country and its short name
    #.str[0] - takes the first column only discarding the country short names column
    #.str.strip() - removes the extra space at the end of our country column
    
    return dataframe

#Call to the function
q02_country_operations(OlympicsDF).head(150)









