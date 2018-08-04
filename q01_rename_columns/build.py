import pandas as pd
import numpy as np


str_path='data/olympics.csv'

def q01_rename_columns(path):
	df = pd.read_csv(path,skiprows=1, delimiter=',' , dtype='|S10')
	df.rename(columns={'Unnamed: 0': 'Country', '01 !' : 'Gold_Summer', '02 !':'Silver_Summer','03 !' : 'Bronze_Summer',
								'01 !.1' : 'Gold_Winter', '02 !.1':'Silver_Winter','03 !.1' : 'Bronze_Winter',
								'Total' : 'Total_Summer', 'Total.1':'Total_Winter','Combined total' : 'Total',
								'01 !.2' : 'Gold_Total', '02 !.2':'Silver_Total','03 !.2' : 'Bronze_Total'}, inplace=True)
	return df
	
df_olympic = q01_rename_columns(str_path)
print (df_olympic)


