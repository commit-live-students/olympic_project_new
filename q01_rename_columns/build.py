# %load q01_rename_columns/build.py
# default imports
import pandas as pd

def q01_rename_columns(path):
    csv_data = pd.read_csv(path,skiprows=[1])
    df = pd.DataFrame(csv_data,columns=['Country', '# Summer', 'Gold_Summer', 'Silver_Summer',
       'Bronze_Summer', 'Total_Summer', '# Winter', 'Gold_Winter',
       'Silver_Winter', 'Bronze_Winter', 'Total_Winter', '# Games',
       'Gold_Total', 'Silver_Total', 'Bronze_Total', 'Total'])
    return df

q01_rename_columns('./data/olympics.csv')





