import pandas as pd
import numpy as np


str_path='data/olympics.csv'

def q01_rename_columns(path):
	df = pd.read_csv(path,skiprows=1, delimiter=',' )
	df.rename(columns={'Unnamed: 0': 'Country', '01 !' : 'Gold_Summer', '02 !':'Silver_Summer','03 !' : 'Bronze_Summer',
								'01 !.1' : 'Gold_Winter', '02 !.1':'Silver_Winter','03 !.1' : 'Bronze_Winter',
								'Total' : 'Total_Summer', 'Total.1':'Total_Winter','Combined total' : 'Total',
								'01 !.2' : 'Gold_Total', '02 !.2':'Silver_Total','03 !.2' : 'Bronze_Total'}, inplace=True)
	return df

def exrtact_name(df_country):
    print('inside extract name function')
    vLen = df_country['Country'].str.find('(')
    print(vLen)

def SubString(str1):
    str2 = '('
    CharFindPosition = str1.find(str2)
    return_String = str1[:CharFindPosition]
    return return_String.strip()

def q02_country_operations(OlympicsDF):
    df = OlympicsDF['Country']
    df = df.apply(SubString)
    OlympicsDF['Country_Name'] = df
    return OlympicsDF

df_olympic = q01_rename_columns(str_path)
q02_country_operations(df_olympic)



