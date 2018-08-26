# %load q01_rename_columns/build.py
# default imports
import pandas as pd
def q01_rename_columns(self):
    col_names = ['Country', '# Summer', 'Gold_Summer', 'Silver_Summer',
      'Bronze_Summer', 'Total_Summer', '# Winter', 'Gold_Winter',
      'Silver_Winter', 'Bronze_Winter', 'Total_Winter', '# Games',
      'Gold_Total', 'Silver_Total', 'Bronze_Total', 'Total']
    raw_data = pd.read_csv('./data/olympics.csv', skiprows = [0])
    df = pd.DataFrame(raw_data)    
    df.columns = col_names
    return df








