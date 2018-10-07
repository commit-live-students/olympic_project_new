# %load q04_find_top_10/build.py
# default imports
import pandas as pd
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df, col1, col2, col3):
    df = df[df.Country_Name != 'Totals']
    summer = df.nlargest(10, col1)['Country_Name']
    winter = df.nlargest(10, col2)['Country_Name']
    both = df.nlargest(10, col3)['Country_Name']
    intersection = pd.Series(list(set(summer).intersection(set(winter))))
    return summer,winter,both,pd.Series(list(set(intersection).intersection(set(both))))

s1,s2,s3,s4 = q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
s1
s2
s3



