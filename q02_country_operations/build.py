# %load q02_country_operations/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(data):
    
    testing_col = data['Country']
    temp_result = []
    for value in testing_col:
        temp_result.append(value.split()[0])

    data['Country_Name'] = pd.Series(temp_result)
    
    return data


q02_country_operations(OlympicsDF)



