# %load q01_rename_columns/build.py
# default imports
import pandas as pd
def q01_rename_columns(path):
    df = pd.read_csv(path , skiprows = 1)
    df.columns.values[0] = 'Country'
    
    for x in range(0 , len(df.columns.values)):
        if df.columns.values[x] == '# Summer':
            df.columns.values[x+1] = 'Gold_Summer'
            df.columns.values[x+2] = 'Silver_Summer'
            df.columns.values[x+3] = 'Bronze_Summer'
            df.columns.values[x+4] = 'Total_Summer'
        elif df.columns.values[x] == '# Winter':
            df.columns.values[x+1] = 'Gold_Winter'
            df.columns.values[x+2] = 'Silver_Winter'
            df.columns.values[x+3] = 'Bronze_Winter'
            df.columns.values[x+4] = 'Total_Winter'
        elif df.columns.values[x] == '# Games': 
            df.columns.values[x+1] = 'Gold_Total'
            df.columns.values[x+2] = 'Silver_Total'
            df.columns.values[x+3] = 'Bronze_Total'
            df.columns.values[x+4] = 'Total'
            
    return df


