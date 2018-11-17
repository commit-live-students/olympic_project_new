# %load q02_country_operations/build.py
# default imports
#from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions


import pandas as pd

path = './data/olympics.csv'


def q01_rename_columns(path):
    df=pd.read_csv(path,skiprows=1)
    df.rename(columns={'Unnamed: 0': 'Country',
                   '01 !':'Gold_Summer' ,
                   '02 !':'Silver_Summer',
                   '03 !':'Bronze_Summer',
                   'Total':'Total_Summer', 
                   '01 !.1': 'Gold_Winter',
                   '02 !.1': 'Silver_Winter' ,
                   '03 !.1' : 'Bronze_Winter',
                   'Total.1':'Total_Winter',
                   '01 !.2' :'Gold_Total',
                   '02 !.2': 'Silver_Total',
                   '03 !.2':'Bronze_Total',
                   'Combined total' :'Total'
                  },inplace=True)
    return df

OlympicsDF=q01_rename_columns(path)  

def q02_country_operations(df=OlympicsDF):
    df['Country_Name']=df.Country.str.split('(').str[0].str.strip()
    #To remove white space at both ends:str.strip()
    #To separate the str on basis of '(' str.split() function is used
    return df


q02_country_operations(OlympicsDF)




