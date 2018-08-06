# %load q02_country_operations/build.py
# default imports
import numpy as np
import pandas as pd
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(OlympicsDF):
    OlympicsDF['Country Name'] = OlympicsDF['Country']
    OlympicsDF['Country Name']=OlympicsDF['Country Name'].apply(lambda x : (x.split('(')[0]).replace(u'\xa0', u''))
    return OlympicsDF



q02_country_operations(OlympicsDF)








