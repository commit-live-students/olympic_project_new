# %load q01_rename_columns/build.py
# default imports
import pandas as pd

def q01_rename_columns(path):
    data = pd.read_csv(path, skiprows=[0])
    
    data.rename(columns={'Unnamed: 0':'Country'}, inplace=True)
    data.columns.values[2] = 'Gold_Summer'
    data.columns.values[3] = 'Silver_Summer'
    data.columns.values[4] = 'Bronze_Summer'
    data.columns.values[5] = 'Total_Summer'
    
    data.columns.values[7] = 'Gold_Winter'
    data.columns.values[8] = 'Silver_Winter'
    data.columns.values[9] = 'Bronze_Winter'
    data.columns.values[10] = 'Total_Winter'
    
    data.columns.values[12] = 'Gold_Total'
    data.columns.values[13] = 'Silver_Total'
    data.columns.values[14] = 'Bronze_Total'
    data.columns.values[15] = 'Total'
    
    return data




