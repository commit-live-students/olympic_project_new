# %load q01_rename_columns/build.py
# default imports
import pandas as pd
path = './data/olympics.csv'
def q01_rename_columns(path):
    csv_file = pd.read_csv(path, skiprows=1)
    csv_file.rename(columns = {'Unnamed: 0':'Country'}, inplace = True)
    csv_file.rename(columns = {'01 !':'Gold_Summer','02 !':'Silver_Summer','03 !':'Bronze_Summer'}, inplace=True)
    csv_file.rename(columns = {'Total':'Total_Summer','Total.1':'Total_Winter','Combined total':'Total'},inplace=True)
    csv_file.rename(columns = {'01 !.1':'Gold_Winter','02 !.1':'Silver_Winter','03 !.1':'Bronze_Winter'},inplace=True)
    csv_file.rename(columns = {'01 !.2':'Gold_Total','02 !.2':'Silver_Total','03 !.2':'Bronze_Total'},inplace=True)
    return(csv_file)

q01_rename_columns(path)






