# %load q01_rename_columns/build.py
# default imports
import pandas as pd




path = './data/olympics.csv'



olympics = pd.read_csv('./data/olympics.csv',skiprows= [1])
olympics1 = pd.read_csv('./data/olympics.csv',skiprows= [1])
df = pd.DataFrame(olympics1)

df

def q01_rename_columns (path):
    df = pd.DataFrame(olympics1)
    df = df.rename(columns = {'0':'Country','1':'# Summer','6':'# Winter','11':'# Games'})
    df = df.rename(columns = {'2':'Gold_Summer','3':'Silver_Summer','4':'Bronze_Summer'})
    df = df.rename(columns = {'7':'Gold_Winter','8':'Silver_Winter','9':'Bronze_Winter'})
    df = df.rename(columns = {'12':'Gold_Total','13':'Silver_Total','14':'Bronze_Total'})
    df = df.rename(columns = {'5' : 'Total_Summer','10' : 'Total_Winter','15' : 'Total'})
    return df


q01_rename_columns(path)



