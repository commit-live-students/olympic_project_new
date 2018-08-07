# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(df, low, high):
    df.drop(df.tail(1).index,inplace=True)
    quant_df = OlympicsDF['Total'].quantile([low, high])
    DFHigh = df.loc[df['Total']>=quant_df.loc[high],['Country_Name']]
    DFLow = df.loc[df['Total']<=quant_df.loc[low], ['Country_Name']]
    return DFLow, DFHigh



