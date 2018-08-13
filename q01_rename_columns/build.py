# %load q01_rename_columns/build.py
# default imports
import pandas as pd
import numpy as np

path = './data/olympics.csv'

def q01_rename_columns(path):
    data1=pd.read_csv(path,skiprows=1) #skips 1st row
    data1.rename(index=str,columns ={'Unnamed: 0':'Country','01 !':'Gold_Summer','02 !':'Silver_Summer','03 !':'Bronze_Summer','01 !.1':'Gold_Winter','02 !.1':'Silver_Winter','03 !.1':'Bronze_Winter','Total':'Total_Summer','Total.1':'Total_Winter','Combined total':'Total'},inplace=True)#renames columns
    data1.rename(index=str,columns={'01 !.2':'Gold_Total', '02 !.2':'Silver_Total', '03 !.2':'Bronze_Total'},inplace=True)#renames columns
    return data1

q01_rename_columns(path)

