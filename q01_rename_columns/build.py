# %load q01_rename_columns/build.py
# default imports
import pandas as pd

def q01_rename_columns(path):
    data = pd.read_csv(path , skiprows=[0])
    #data = data.drop(1)
    
    data1 = pd.DataFrame(data)
    data1 = data1.rename(columns={data1.columns[0]: 'Country'})
    new_cols=['Gold_Summer','Silver_Summer','Bronze_Summer','Total_Summer','# Winter','Gold_Winter','Silver_Winter','Bronze_Winter','Total_Winter','# Games','Gold_Total','Silver_Total','Bronze_Total','Total']
    data1.rename(columns=dict(zip(data1.columns[2:], new_cols)),inplace=True)
    
    
    
    
    
    return data1

q01_rename_columns('./data/olympics.csv')




