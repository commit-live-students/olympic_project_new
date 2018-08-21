# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
import pandas as pd

low = 0.05
high = 0.95

quant_df = OlympicsDF['Total'].quantile([low,high])

def q07_unusual_performances(df, lowQuantile, highQuantile):
    df.drop(df.tail(1).index , inplace=True)
    df[(df['Total']<= lowQuantile)]
    a = pd.DataFrame(df[(df['Total']<=lowQuantile)])
    b = pd.DataFrame(df[(df['Total']>highQuantile)])
    return a['Country_Name'] , b['Country_Name']

a,b = q07_unusual_performances(OlympicsDF,quant_df.loc[low],quant_df.loc[high])



