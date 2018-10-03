# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
import numpy as np
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
def q07_unusual_performances(df=OlympicsDF,high=0.95,low=0.05):
    q1=df['Total'].quantile(low)
    q2=df['Total'].quantile(high)
    df=df[df['Country']!='Totals']
    lowcons=list(df[df['Total']<=q1]['Country_Name'])
    highcons=list(df[df['Total']>q2]['Country_Name'])
    return lowcons,highcons





