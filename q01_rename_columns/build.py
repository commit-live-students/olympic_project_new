# %load q01_rename_columns/build.py
# default imports
import pandas as pd
path = './data/olympics.csv'

def q01_rename_columns(path):
    df = pd.read_csv(path,skiprows = 1)
    df.rename(columns={df.columns[0]: 'Country'},inplace =True)
                      #'01 !': 'Gold_Summer','02 !': 'Silver_Summer','03 !': 'Bronze_Summer'})
    #df.columns = df.columns.str.replace('01!*': 'Gold_Summer')
   # df.columns = df.columns.str.replace('02!*': 'Silver_Summer')
   # df.columns = df.columns.str.replace('03!*': 'Bronze_Summer')
    df.rename(columns={'Total': 'Total_Summer', 
                       'Total.1': 'Total_Winter', 
                       'Combined total': 'Total', 
                       '01 !': 'Gold_Summer',
                       '02 !': 'Silver_Summer',
                       '03 !': 'Bronze_Summer',
                        '01 !.1': 'Gold_Winter',
                       '02 !.1': 'Silver_Winter',
                       '03 !.1': 'Bronze_Winter',
                       '01 !.2': 'Gold_Total',
                       '02 !.2': 'Silver_Total',
                       '03 !.2': 'Bronze_Total',
                
                  },inplace = True)
    return df




