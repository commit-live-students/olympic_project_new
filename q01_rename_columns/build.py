# %load q01_rename_columns/build.py
# default imports
import pandas as pd
# %load q01_rename_columns/build.py
# default imports

path = './data/olympics.csv'
def q01_rename_columns(path):

    olympic_df = pd.read_csv (path, skiprows = 1)
    olympic_df.rename(columns={'Unnamed: 0':'Country'}, inplace = True)
# Summer
    olympic_df.rename(columns={'01 !':'Gold_Summer'}, inplace  = True)
    olympic_df.rename(columns={'02 !':'Silver_Summer'}, inplace  = True)
    olympic_df.rename(columns={'03 !':'Bronze_Summer'}, inplace  = True)
#Winter
    olympic_df.rename(columns={'01 !.1':'Gold_Winter'}, inplace  = True)
    olympic_df.rename(columns={'02 !.1':'Silver_Winter'}, inplace  = True)
    olympic_df.rename(columns={'03 !.1':'Bronze_Winter'}, inplace  = True)
#Games
    olympic_df.rename(columns={'01 !.2':'Gold_Total'}, inplace  = True)
    olympic_df.rename(columns={'02 !.2':'Silver_Total'}, inplace  = True)
    olympic_df.rename(columns={'03 !.2':'Bronze_Total'}, inplace  = True)
#Total
    olympic_df.rename(columns={'Total':'Total_Summer'}, inplace  = True)
    olympic_df.rename(columns={'Total.1':'Total_Winter'}, inplace  = True)
    olympic_df.rename(columns={'Combined total':'Total'}, inplace  = True)

    return olympic_df
q01_rename_columns(path)




