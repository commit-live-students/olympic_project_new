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
	#print('inside extract name function')
	vLen = df_country['Country'].str.find('(')
	#print(vLen)

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

def CompareMedals(Medals):
	print ('iSummer : ',Medals['Total_Summer'] , '  ---> iWinter : ',Medals['Total_Winter'])
	if Medals['Total_Summer'] > Medals['Total_Winter']:
		return 'Summer'
	else:
		return 'Winter'

def CompareMedals1(iMedals):
    #print('iMedals : ',iMedals)
    if (iMedals >0):
        return 'Summer'
    elif (iMedals<0):
        return 'Winter'
    else:
        return 'Both'
    
    
def q03_better_event(OlympicsDF):
    #print('Country : ', OlympicsDF['Country_Name'] , ' ---> Summer : ' , OlympicsDF['Total_Summer'] , '    ----> Winter ' ,OlympicsDF['Total_Winter'])
    #lstMedals = [OlympicsDF['Total_Summer'],OlympicsDF['Total_Winter']]
    #OlympicsDF['BetterEvent'] = map(CompareMedals1 , (OlympicsDF['Total_Summer'],OlympicsDF['Total_Winter']) )
    #OlympicsDF['BetterEvent'] = lambda  OlympicsDF['Total_Summer'],OlympicsDF['Total_Winter']: CompareMedals1)
    #print ('Better Event : ',OlympicsDF['BetterEvent'])
    #OlympicsDF['BetterEvent'] = map(CompareMedals ,(5,7))
    OlympicsDF['BetterEvent'] = OlympicsDF['Total_Summer'] - OlympicsDF['Total_Winter']
    OlympicsDF['BetterEvent'] = OlympicsDF['BetterEvent'].apply(CompareMedals1)
    return OlympicsDF
	
	




#y = map(multiply2, [1, 2, 3, 4]) 
#print(list(y))
df_olympic = q01_rename_columns(str_path)
df_olympic = q02_country_operations(df_olympic)
#print('Before Better event')
df_olympic = q03_better_event(df_olympic)
#print('After Better event : ',df_olympic['BetterEvent'])




