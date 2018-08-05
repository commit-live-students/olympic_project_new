# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
import pandas as pd
import numpy as np
def q02_country_operations(OlympicsDF=q01_rename_columns(path)):
    df=pd.DataFrame(OlympicsDF)
    df['Country Name']=df['Country']
    b=[]
    for i in df['Country Name']:
        d=i.split('(')#returns a list always
        b.append(d[0].strip())#\xao is a space so we have stripped it off
    b=pd.DataFrame(b)
    df['Country Name']=b
    df['Country Name']=pd.Series.to_frame(df['Country Name'])
    return df


    




c=q02_country_operations(OlympicsDF=q01_rename_columns(path))
c


