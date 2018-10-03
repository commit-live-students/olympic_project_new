# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
import numpy as np
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
def q07_unusual_performances(df=OlympicsDF,low=0.05,high=0.95):
    df=df[df['Country']!='Totals']
    q1=df['Total'].quantile(low)
    q2=df['Total'].quantile(high)
    lowcons=df[df['Total']<=q1]['Country_Name']
    highcons=df[df['Total']>=q2]['Country_Name']
    return lowcons,highcons
q07_unusual_performances(df=OlympicsDF,low=0.05,high=0.95)




