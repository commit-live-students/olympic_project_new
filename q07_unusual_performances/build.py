# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
low = 0.05
high =0.95

def q07_unusual_performances(df, low, high):
    df = df[:-1]
    low_q, high_q = df['Total'].quantile([0.05,0.95])
    var1 = df[df['Total'] <= low_q]['Country_Name']
    var2 = df[df['Total'] > high_q]['Country_Name']
    var2 = var2[1:]
#     print(var1,var2)
    return var1, var2

print(q07_unusual_performances(OlympicsDF, low, high))

# OlympicsDF.tail()


