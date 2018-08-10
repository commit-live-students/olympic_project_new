# %load q01_rename_columns/build.py
# default imports
import pandas as pd
def q01_rename_columns(path):
    data=pd.read_csv(path,skiprows=1)
    data.columns=['Country', '# Summer', 'Gold_Summer', 'Silver_Summer',
       'Bronze_Summer', 'Total_Summer', '# Winter', 'Gold_Winter',
       'Silver_Winter', 'Bronze_Winter', 'Total_Winter', '# Games',
       'Gold_Total', 'Silver_Total', 'Bronze_Total', 'Total']
  

   
    return data









