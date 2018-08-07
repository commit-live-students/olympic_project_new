# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

low=0.05
high=0.95
quant_df = OlympicsDF['Total'].quantile([low, high])

def q07_unusual_performances(df, low=0.000, high=0.000):
    df.drop(df.tail(1).index,inplace=True)
    
    DFHigh = df.loc[df['Total']>=high,['Country_Name']]
    DFLow = df.loc[df['Total']<=low, ['Country_Name']]
    return DFLow['Country_Name'].tolist(), DFHigh['Country_Name'].tolist()




