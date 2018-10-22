# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)


low = 0.05
high = 0.95
def q07_unusual_performances(variable1, variable2, variable3):
    
    var2 = OlympicsDF[OlympicsDF['Total'] > OlympicsDF['Total'].quantile(0.95) ].drop(146)
    var3 = OlympicsDF[OlympicsDF['Total'] <= OlympicsDF['Total'].quantile(0.05)]

    return var3['Country_Name'],var2['Country_Name']
    
    
q07_unusual_performances(OlympicsDF, low, high)




