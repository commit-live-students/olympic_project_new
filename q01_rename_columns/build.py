# %load q01_rename_columns/build.py
# default imports
import pandas as pd
path = 'data/olympics.csv'

def q01_rename_columns(path):
    data1 = pd.read_csv(path,skiprows=[0])
    df=pd.DataFrame(data1)
    return df.rename(columns={'Unnamed: 0':'Country','01 !':'Gold_Summer','02 !':'Silver_Summer','03 !':'Bronze_Summer','Total':'Total_Summer','01 !.1':'Gold_Winter','02 !.1':'Silver_Winter','03 !.1':'Bronze_Winter','Total.1':'Total_Winter','01 !.2':'Gold_Total','02 !.2':'Silver_Total','03 !.2':'Bronze_Total','Combined total':'Total'})
    


q01_rename_columns(path)



