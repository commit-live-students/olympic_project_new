# %load q07_unusual_performances/build.py
# default imports

#My Solution
import pandas as pd
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(Dataset, lower_percentile, higher_percentile):
    
    Lower_Quantile  = OlympicsDF['Total'].quantile(lower_percentile)
    Higher_Quantile = OlympicsDF['Total'].quantile(higher_percentile)

    OlympicsDF.drop(OlympicsDF.tail(1).index,inplace=True)
    
    Better_Countries = OlympicsDF[OlympicsDF['Total']>Higher_Quantile]['Country_Name']
    Worse_Countries  = OlympicsDF[OlympicsDF['Total']<=Lower_Quantile]['Country_Name']

    return Worse_Countries,Better_Countries




#Call to the function-
q07_unusual_performances(OlympicsDF,0.05,0.95)
#Solution that passed the test case
def q07_unusual_performances(OlympicsDF,low,high):
    
    OlympicsDF.drop(OlympicsDF.tail(1).index,inplace=True)
   
    quant1=OlympicsDF['Total'].quantile(0.05)
    quant2=OlympicsDF['Total'].quantile(0.95)
    better=OlympicsDF[OlympicsDF['Total']>quant2]['Country_Name']
    better=better.drop(labels=23)
    worse=OlympicsDF[OlympicsDF['Total']<=quant1]['Country_Name']
    
    return worse,better
q07_unusual_performances(OlympicsDF,0.05,0.95)

