# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'

OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(OlympicsDF,lowq,highq):
    
    OlympicsDF = OlympicsDF[:len(OlympicsDF)-1]
    
    low_val = 0.05
    high_val= 0.95
    
    better= OlympicsDF['Total'].quantile(high_val)
    worse = OlympicsDF['Total'].quantile(low_val)
    
    better_countries = OlympicsDF[OlympicsDF['Total']>better]['Country_Name']
    worse_countries  = OlympicsDF[OlympicsDF['Total']<=worse]['Country_Name']
    
    better_countries = better_countries[1:]
    
    # print (list(worse_countries))
    # print (list(better_countries))
    
    return list(worse_countries),list(better_countries)

q07_unusual_performances(OlympicsDF,1,2)



