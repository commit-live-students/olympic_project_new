# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(OlympicsDF,low, high):
      
        
    df =OlympicsDF[:-1]
    #quant_df = df['Total'].quantile([low, high])
    df_low= df[low >= df['Total']]['Country_Name']
    df_high=df[high <= df['Total']]['Country_Name']
    return df_low,df_high






