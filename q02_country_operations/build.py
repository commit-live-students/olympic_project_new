# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
import pandas as pd
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)

def q02_country_operations(OlympicsDF):
    data = OlympicsDF.astype(str)
    first_words = data.apply(lambda x: x.str.split().str[0])
    first_words['Country_Name'] = first_words['Country']
    return first_words
    



