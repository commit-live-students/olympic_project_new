# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

#Define the function 
def q04_find_top_10(OlympicsDF,Total_Summer,Total_Winter,Total):
    '''Function to extract Top 10 countries'''
    #Drop the Totals 
    OlympicsDF.drop(axis=0,labels=146,inplace=True)

    #Creating list for Top 10 countries
    Top10_Total = list(OlympicsDF[['Country_Name',Total]].sort_values(by='Total',ascending = False).head(10)['Country_Name'])
    Top10_Winter = list(OlympicsDF[['Country_Name',Total_Winter]].sort_values(by='Total_Winter',ascending = False).head(10)['Country_Name'])
    Top10_Summer = list(OlympicsDF[['Country_Name',Total_Summer]].sort_values(by='Total_Summer',ascending = False).head(10)['Country_Name'])
    Common = list(set(Top10_Summer).intersection(Top10_Total,Top10_Winter)) #Using intersection will get common values
    return Top10_Summer,Top10_Winter, Top10_Total, Common 

#Function Call
q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')

OlympicsDF


