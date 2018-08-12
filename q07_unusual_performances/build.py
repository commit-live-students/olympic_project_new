# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(OlympicsDF,lowq,highq):
    OlympicsDF = OlympicsDF[:len(OlympicsDF)-1]
    high= OlympicsDF['Total'].quantile(0.95)
    low = OlympicsDF['Total'].quantile(0.05)
    high_countries = OlympicsDF[OlympicsDF['Total']>high]['Country_Name']
    low_countries = OlympicsDF[OlympicsDF['Total']<=low]['Country_Name']
    high_countries = high_countries[1:]
    return list(low_countries),list(high_countries)
#q07_unusual_performances(OlympicsDF,1,2)

