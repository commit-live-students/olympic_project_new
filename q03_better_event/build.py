# %load q03_better_event/build.py
#default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import numpy as np
#Previous function
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)



def q03_better_event(OlympicsDF=OlympicsDF):
    OlympicsDF.loc[OlympicsDF.loc[:,'Total_Winter']<OlympicsDF.loc[:,'Total_Summer'],'BetterEvent']='Summer'
    OlympicsDF.loc[OlympicsDF.loc[:,'Total_Winter']>OlympicsDF.loc[:,'Total_Summer'],'BetterEvent']='Winter'
    OlympicsDF.loc[OlympicsDF.loc[:,'Total_Winter']==OlympicsDF.loc[:,'Total_Summer'],'BetterEvent']='Both'
   
    return OlympicsDF



df=OlympicsDF
cond =[ df['Total_Summer'] == df['Total_Winter'],df['Total_Summer'] > df['Total_Winter'],df['Total_Summer'] < df['Total_Winter']]
choice = ['Both','Summer', 'Winter']
import numpy as np
x=np.select(cond,choice)
import pandas as pd
x=pd.Series(x)
x.value_counts()
df['BetterEvent']=x
df

























