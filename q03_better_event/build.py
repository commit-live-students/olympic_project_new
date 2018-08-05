# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
import pandas as pd
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q03_better_event(q02_country_operations):
    df=OlympicsDF
    df['BetterEvent']=np.where((df['Total_Summer']>df['Total_Winter']),
                               'Summer',np.where(df['Total_Summer']<df['Total_Winter'],'Winter','Both'))# or (df['Total_Summer']<df['Total_Winter']) or (df['Total_Summer'] == df['Total_Winter']),df['Better Event'],np.nan)
    return df
#     b=[]
#     for i in df['Total_Summer']:
#         for j in df['Total_Winter']:
#             for k in df['Total']:
#                 if (i>j) & (i>k):
#                     b.append(i)
#                 elif (j>i) & (j>k):
#                     b.append(j)
#                 else:
#                     b.append(k)
     
    







c=q03_better_event(q02_country_operations)

c


