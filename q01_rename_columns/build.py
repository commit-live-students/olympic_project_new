# %load q01_rename_columns/build.py
# default imports
import pandas as pd
path = 'data/olympics.csv'
def q01_rename_columns(path):
    df = pd.read_csv(path,skiprows=1)
    df2 = df.rename(columns={'Unnamed: 0':'Country','01 !':'Gold_Summer','01 !.1':'Gold_Winter','01 !.2':'Gold_Total','02 !':'Silver_Summer','02 !.1':'Silver_Winter','02 !.2':'Silver_Total','03 !':'Bronze_Summer','03 !.1':'Bronze_Winter','03 !.2':'Bronze_Total','Total':'Total_Summer','Total.1':'Total_Winter','Combined total':'Total'})
    return df2
q01_rename_columns(path)


