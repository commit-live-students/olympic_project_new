# %load q07_unusual_performances/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
import numpy as np

# def q07_unusual_performances(OlympicsDF,low=0.05,high=0.95):
#     df=OlympicsDF
#     a=df['Total']/100
#     q=df['Total'].quantile([low,high])
#     b=[]
#     for i,j in zip(df['Total'],df['Country_Name']):
#         if i>(q[high]):
#             b.append(j)
#     c=[]
#     for i,j in zip(df['Total'],df['Country_Name']):
#         if i==(q[low]):
#             c.append(j)
#     return pd.DataFrame([b,c])
    
low=0.05
high=0.95

quantile_df=OlympicsDF['Total'].quantile([low,high])

def q07_unusual_performances(df,lower_quantile,upper_quantile):
    df.drop(df.tail(1).index,inplace=True)
    
    good_countries=pd.DataFrame(df[df['Total']>upper_quantile])
    bad_countries=pd.DataFrame(df[df['Total']<=lower_quantile])
    
    return bad_countries['Country_Name'],good_countries['Country_Name']
    
            
    
        

        
    
    
    

c=q07_unusual_performances(OlympicsDF,quantile_df[low],quantile_df[high])
c








