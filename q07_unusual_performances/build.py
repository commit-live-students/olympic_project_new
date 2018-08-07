# %load q07_unusual_performances/build.py
# default imports

from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import pandas as pd

path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
import pandas as pd

low=0.05
high=0.95

quantile_df = OlympicsDF['Total'].quantile([low, high])

def q07_unusual_performances(df, lower_quantile, upper_quantile):
    df.drop(df.tail(1).index,inplace=True)

    good_countries = pd.DataFrame(df[df['Total']>upper_quantile])
    bad_countries = pd.DataFrame(df[df['Total']<=lower_quantile])

    return bad_countries['Country_Name'], good_countries['Country_Name']

q07_unusual_performances(OlympicsDF,quantile_df.iloc[0], quantile_df.iloc[1])




