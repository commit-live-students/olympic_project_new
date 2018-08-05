# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
import pandas as pd
import re
re.compile('<title>(.*)</title>')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

# def q02_country_operations(df):
#     df['Country Name']=df['Country'][:] 
#     df['Country name']=(df['Country Name'].str.split('(',1).str)[0].str.strip
    
#     return df
# # q02_country_operations(OlympicsDF).iloc[100,16]
# q02_country_operations(OlympicsDF).iloc[100,16]
# #print(OlympicsDF.iloc[100,16])
def q02_country_operations(OlympicsDF):
    country_name = []
    for country  in OlympicsDF['Country']:
        position = re.search('\(',country)
        if position!=None:
            country_name.append(country[:position.end()-2])
        else:
            country_name.append(country)
    OlympicsDF['Country Name'] = pd.Series(country_name)
    return OlympicsDF


q02_country_operations(OlympicsDF)





