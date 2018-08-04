# %load q01_rename_columns/build.py
# default imports
import pandas as pd

def q01_rename_columns(path):
    data=pd.read_csv(path,skiprows=[0])
#     data=pd.DataFrame(data)
#     data=data.drop(0)
   
    data=data.rename(columns={data.columns[0]:'Country'})
    my_list=['Gold_Summer','Silver_Summer','Bronze_Summer','Total_Summer','# Winter','Gold_Winter','Silver_Winter','Bronze_Winter','Total_Winter','# Games','Gold_Total','Silver_Total','Bronze_Total','Total']
    data=data.rename(columns=dict(zip(data.columns[2:],my_list)))
    
    return data
q01_rename_columns('./data/olympics.csv')






