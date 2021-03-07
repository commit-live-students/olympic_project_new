# %load q01_rename_columns/build.py
# default imports
import pandas as pd

path='./data/olympics.csv'

def q01_rename_columns(path):
    
    df=pd.read_csv(path,skiprows=[0])
    df.rename(columns={'Combined total':'Total','Total.1':'Total_Winter','Total':'Total_Summer'},inplace=True)
    df.columns.values[0] = 'Country'
    df.columns = df.columns.str.replace('01 !', 'Gold_Summer')
    df.columns = df.columns.str.replace('02 !', 'Silver_Summer')
    df.columns = df.columns.str.replace('03 !', 'Bronze_Summer')
    df.columns = df.columns.str.replace('Summer.1', 'Winter') 
    df.columns = df.columns.str.replace('Summer.2', 'Total')
    return df


