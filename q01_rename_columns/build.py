# %load q01_rename_columns/build.py
# default imports
import pandas as pd

path = './data/olympics.csv'

def q01_rename_columns(path):
    
    df= pd.read_csv(path,skiprows=1)
    df.rename(columns={'Unnamed: 0': 'Country'}, inplace= True)
    df.rename(columns={'Total': 'Total_Summer'}, inplace= True)
    df.rename(columns={'Total.1': 'Total_Winter'}, inplace= True)
    df.rename(columns={'Combined total': 'Total'}, inplace= True)

    for index,x in enumerate(df.columns):
        if '01'in x:
            name = df.columns[index-1][1:]
            if 'Games' in name:
                name = 'Total'
            df.rename(columns={x:'Gold'+'_'+str.strip(name)}, inplace=True)
        if '02'in x:
            name = df.columns[index-2][1:]
            if 'Games' in name:
                name = 'Total'
            df.rename(columns={x:'Silver'+'_'+str.strip(name)}, inplace=True)
        if '03'in x:
            name = df.columns[index-3][1:]
            if 'Games' in name:
                name= 'Total'
            df.rename(columns={x:'Bronze'+'_'+str.strip(name)}, inplace=True)
        
    return df


