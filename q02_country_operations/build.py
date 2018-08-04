# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
import re
import pandas as pd
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

# my solution

def q02_country_operations(OlympicsDF):
    country_name = []
    for country  in OlympicsDF['Country']:
        position = re.search('\(',country)
        if position!=None:
            country_name.append(country[:position.end()-2])
        else:
            country_name.append(country)
    OlympicsDF['Country Name'] = pd.Series(country_name)
    #print (OlympicsDF)
    return OlympicsDF

#q02_country_operations(OlympicsDF)




