# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(df, low, high):
    #OlympicsDF = OlympicsDF[:146]
    low = 0.05
    high = 0.95
    t = list(OlympicsDF.Total.quantile([low,high]))
        
    #quant_df = df['Total'].quantile([low, high])
    #DFLow, DFHigh= q07_unusual_performances(df, quant_df.loc[low], quant_df.loc[high])
    df1 = OlympicsDF[OlympicsDF['Total']<(int(t[0])+1)]
    df2= OlympicsDF[OlympicsDF['Total']>(int(t[1])-1)]
    df2 = df2[:-1]
    return df1['Country_Name'],df2['Country_Name']







