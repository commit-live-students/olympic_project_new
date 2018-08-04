# %load q01_rename_columns/build.py
# default imports
import pandas as pd

path = './data/olympics.csv'

def q01_rename_columns(path):
    df = pd.read_csv(path, skiprows=1)
    df.rename(columns={'Unnamed: 0':'Country'},inplace=True)
    df.rename(columns={'01 !':'Gold_Summer','02 !':'Silver_Summer','03 !':'Bronze_Summer', 'Total':'Total_Summer'},inplace=True)
    df.rename(columns={'01 !.1':'Gold_Winter','02 !.1':'Silver_Winter','03 !.1':'Bronze_Winter', 'Total.1':'Total_Winter'},inplace=True)
    df.rename(columns={'01 !.2':'Gold_Total','02 !.2':'Silver_Total','03 !.2':'Bronze_Total', 'Combined total':'Total'},inplace=True)

    return df

q01_rename_columns(path)


