# %load q01_rename_columns/build.py
# default imports
import pandas as pd

path='./data/olympics.csv'

def q01_rename_columns(path):
    df=pd.read_csv(path,header=0)
    #b.Skips first row.
    dx=df[1:]
    dx.rename(columns = {'0':'Country', '1': '# Summer', '2':'Gold_Summer','3': 'Silver_Summer',
       '4':'Bronze_Summer', '5':'Total_Summer', '6':'# Winter', '7':'Gold_Winter',
       '8':'Silver_Winter', '9':'Bronze_Winter', '10':'Total_Winter', '11':'# Games',
       '12':'Gold_Total','13': 'Silver_Total','14' :'Bronze_Total','15' :'Total'},inplace=True)

    return dx

q01_rename_columns(path)



