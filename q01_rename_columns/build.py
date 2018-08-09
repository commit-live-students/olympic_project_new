# %load q01_rename_columns/build.py
# default imports
import pandas as pd

def q01_rename_columns(path):
    df = pd.read_csv(path, skiprows=[0])
    
    for index, value in enumerate(df.columns):
        if '01' in value:
            if not 'Games' in df.columns[index-1][1:]:
                df.rename(columns = {value: 'Gold_' + df.columns[index-1][2:]}, inplace = True)
        if '02' in value:
            if not 'Games' in df.columns[index-2][1:]:
                df.rename(columns = {value: 'Silver_' + df.columns[index-2][2:]}, inplace = True)
        if '03' in value:
            if not 'Games' in df.columns[index-3][1:]:
                df.rename(columns = {value: 'Bronze_' + df.columns[index-3][2:]}, inplace = True)
        if 'Total' in value:
            df.rename(columns = {value: 'Total_' + df.columns[index-4][2:]}, inplace = True)
    
    df.rename(columns={ df.columns[0]: 'Country' }, inplace = True)
    df.rename(columns={ df.columns[12]: 'Gold_Total' }, inplace = True)
    df.rename(columns={ df.columns[13]: 'Silver_Total' }, inplace = True)
    df.rename(columns={ df.columns[14]: 'Bronze_Total' }, inplace = True)
    df.rename(columns={ 'Combined total': 'Total' }, inplace = True)
    
    return df
q01_rename_columns('./data/olympics.csv')
#df = pd.read_csv('./data/olympics.csv', skiprows=[0])

# df = pd.read_csv('./data/olympics.csv', skiprows=[0])
# df.columns[14]
# a['Gold_ Summer']
# df.columns[1][2:]



