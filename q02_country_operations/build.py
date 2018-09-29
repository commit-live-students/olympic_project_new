import pandas as pd
import numpy as np
path = './data/olympics.csv'
def q01_rename_columns(path):
    oly_df=pd.read_csv(path,skiprows=1,delimiter=',')
    oly_df.rename(columns={'Unnamed: 0':'Country','01 !':'Gold_Summer','01 !.1':'Gold_Winter','02 !':'Silver_Summer','02 !.1':'Silver_Winter','03 !': 'Bronze_Summer','03 !.1':'Bronze_Winter','Total':'Total_Summer','Total.1':'Total_Winter','01 !.2':'Gold_Total','02 !.2':'Silver_Total','03 !.2':'Bronze_Total','Combined total':'Total'},inplace=True)
    return oly_df
OlympicsDF=q01_rename_columns(path)    
def q02_country_operations(OlympicsDF):
    OlympicsDF['Country_Name']=(OlympicsDF['Country'].str.split('(').str)[0].str.strip()
    return(OlympicsDF)
OlympicsDF['Country_Name']=(OlympicsDF['Country'].str.split('(').str)[0].str.strip()
OlympicsDF.head()


