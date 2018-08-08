# %load q01_rename_columns/build.py
# default imports
import pandas as pd
def q01_rename_columns(olympic):
    olympic = pd.read_csv('./data/olympics.csv',skiprows=1)
    olympic = olympic.rename(columns={'Unnamed: 0':'Country'})
    olympic = olympic.rename(columns={'01 !':'Gold_Summer', '02 !':'Silver_Summer','03 !':'Bronze_Summer', '01 !.1':'Gold_Winter','02 !.1':'Silver_Winter', '03 !.1':'Bronze_Winter','01 !.2':'Gold_Total', '02 !.2':'Silver_Total', '03 !.2':'Bronze_Total'})
    olympic = olympic.rename(columns={'Total':'Total_Summer', 'Total.1':'Total_Winter', 'Combined total':'Total'})
    return olympic




