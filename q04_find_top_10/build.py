# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
import pandas as pd
import numpy as np
def q04_find_top_10(q03_better_event,x='Total_Summer',y='Total_Winter',z='Total'):
    df=OlympicsDF
    a=df.sort_values(by='Total_Summer',ascending=False).head(11)
    a=list(a['Country_Name'][1:11])
    b=df.sort_values(by='Total_Winter',ascending=False).head(11)
    b=list(b['Country_Name'][1:11])
    c=df.sort_values(by='Total',ascending=False).head(11)
    c=list(c['Country_Name'][1:11])
    d=[]
    for i in a:
        for j in b:
            for k in c:
                if (i==j==k):
                    d.append(i)
    return a,b,c,d
    
    
    
    
c=q04_find_top_10(q03_better_event,x='Total_Summer',y='Total_Winter',z='Total')
c


