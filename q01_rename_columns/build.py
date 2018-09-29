# %load q01_rename_columns/build.py
# default imports
path='./data/olympics.csv'
import pandas as pd
def q01_rename_columns(path):
    data=pd.read_csv('./data/olympics.csv',skiprows=1)
    data1=pd.DataFrame(data)
    data1.rename(columns={'Unnamed: 0':'Country','01 !':'Gold_Summer','02 !':'Silver_Summer','03 !':'Bronze_Summer','Total':'Total_Summer','Total.1':'Total_Winter','Combined total':'Total','01 !.1':'Gold_Winter','02 !.1':'Silver_Winter','03 !.1':'Bronze_Winter','01 !.2':'Gold_Total','02 !.2':'Silver_Total','03 !.2':'Bronze_Total'},inplace=True)
    return(data1)

q01_rename_columns(path)






