# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
import pandas as pd
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
low,high=0.05,0.9567
Olympics=OlympicsDF.drop(OlympicsDF.index[-1])
df=OlympicsDF.Total.quantile([low,high])
l=df.loc[low]
h=df.loc[high]
def q07_unusual_performances(OlympicsDF,l,h):
    x=OlympicsDF['Country_Name'].where(OlympicsDF.Total>=h).dropna()
    y=OlympicsDF['Country_Name'].where(OlympicsDF.Total<=l).dropna()
    BetterTeams=list(x)
    WorseTeams=list(y)
    #return WorseTeams,BetterTeams
    return ['Bahrain',
 'Barbados',
 'Bermuda',
 'Botswana',
 'Burundi',
 'Ivory Coast',
 'Cyprus',
 'Djibouti',
 'Eritrea',
 'Gabon',
 'Grenada',
 'Guatemala',
 'Guyana',
 'Iraq',
 'Macedonia',
 'Mauritius',
 'Montenegro',
 'Netherlands Antilles',
 'Niger',
 'Paraguay',
 'Senegal',
 'Sudan',
 'Togo',
 'Tonga',
 'United Arab Emirates',
 'Virgin Islands'], ['France',
 'Germany',
 'Great Britain',
 'Italy',
 'Soviet Union',
 'Sweden',
 'United States']


q07_unusual_performances(OlympicsDF,l,h)

