# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
def q04_find_top_10(data, Col1, Col2, Col3):
    'write your solution here'
    #Remove totals from each medal column
    data=data[data['Country_Name']!='Totals']
    #For Summer
    CountryList1=[]
    CountryList1= list((data.nlargest(10,Col1)['Country_Name']))
    
    #For Winter
    CountryList2=[]
    CountryList2= list((data.nlargest(10,Col2)['Country_Name']))
    
    #Overall
    CountryList3=[]
    CountryList3= list((data.nlargest(10,Col3)['Country_Name']))
    
    #Finding Common
    Common=list(set(CountryList1) & set(CountryList2) & set(CountryList3))
    
    return CountryList1, CountryList2, CountryList3, Common





