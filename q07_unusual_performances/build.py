# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
#Drop the Totals record
#OlympicsDF.drop(labels=146,axis=0,inplace=True)

#Variable assignment
low = 0.05
high = 0.95


    
#Calculate quartile values 
df=OlympicsDF['Total'].quantile([low,high])
low_q = df.loc[low]
high_q = df.loc[high]

#Function Definition
def q07_unusual_performances(OlympicsDF,low_q,high_q):
    ''' Function to get unusual performances in Olympics using quartiles'''

    DFLow = list(OlympicsDF[OlympicsDF['Total'] <= low_q]['Country_Name'])
    DFHigh = list(OlympicsDF[(OlympicsDF['Total'] > high_q) & (OlympicsDF['Country_Name'] != 'Totals')]['Country_Name'])
    return DFLow,DFHigh

#Function call
q07_unusual_performances(OlympicsDF,low_q,high_q)










