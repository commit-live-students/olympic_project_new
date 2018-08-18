# %load q02_country_operations/build.py
# default imports
import pandas as pd
import numpy as np
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'

OlympicsDF=q01_rename_columns(path)


#Function for country operations
def q02_country_operations(OlympicsDF):
    ''' Extract the Country name from Country column and add the same '''
    
    OlympicsDF['Country Name'] = OlympicsDF['Country'].apply(lambda x : x[0:x.index('(')].rstrip() if '(' in x else x )
    return OlympicsDF

#Country call
q02_country_operations(OlympicsDF)

OlympicsDF['Country Name'] = OlympicsDF['Country'].str.split('(')





