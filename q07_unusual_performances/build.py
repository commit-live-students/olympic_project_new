# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(OlympicsDF,low,high):
    
    OlympicsDF.drop(OlympicsDF.tail(1).index,inplace=True)
   
    quant1=OlympicsDF['Total'].quantile(0.05)
    quant2=OlympicsDF['Total'].quantile(0.95)
    better=OlympicsDF[OlympicsDF['Total']>quant2]['Country_Name']
    better=better.drop(labels=23)
    worse=OlympicsDF[OlympicsDF['Total']<=quant1]['Country_Name']
    
    return worse,better

quant1=OlympicsDF['Total'].quantile(0.05)
quant2=OlympicsDF['Total'].quantile(0.95)
better=OlympicsDF[OlympicsDF['Total']>quant2]['Country_Name']
worse=OlympicsDF[OlympicsDF['Total']<=quant1]['Country_Name']

OlympicsDF.drop(OlympicsDF.tail(1).index,inplace=True)
better


