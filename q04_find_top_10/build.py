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

q04_find_top_10(OlympicsDF, 'Total_Summer', 'Total_Winter', 'Total')
'''
# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

# Solution
# Deleting the last row from dataframe since it indicates the 'Totals' of everything
OlympicsDFCopy = OlympicsDF
OlympicsDFCopy = OlympicsDFCopy[:-1]

def q04_find_top_10(OlympicsDFCopy, column_1, column_2, column_3):
    SummerSortedDF = OlympicsDFCopy.sort_values(by=[column_1], ascending=False)
    #print(SummerSortedDF.iloc[1]['Country_Name'])
    indexOfTop10SummerSorted = SummerSortedDF.index[:10].tolist()
    top_10_summer_countries = []
    for index in indexOfTop10SummerSorted:
        top_10_summer_countries.append(OlympicsDFCopy.iloc[index]['Country_Name'])
    top_10_summer_countries.sort()
    
    WinterSortedDF = OlympicsDFCopy.sort_values(by=[column_2], ascending=False)
    index_of_top_10_winter_sorted = WinterSortedDF.index[:10].tolist()
    top_10_winter_countries = []
    for index in index_of_top_10_winter_sorted:
        top_10_winter_countries.append(OlympicsDFCopy.iloc[index]['Country_Name'])
    top_10_winter_countries.sort()
    
    TotalSortedDF = OlympicsDFCopy.sort_values(by=[column_3], ascending=False)
    index_of_top_10_total_sorted = TotalSortedDF.index[:10].tolist()
    top_10_overall_countries = []
    for index in index_of_top_10_total_sorted:
        top_10_overall_countries.append(OlympicsDFCopy.iloc[index]['Country_Name'])
    top_10_overall_countries.sort()
    
    common_countries = set(top_10_summer_countries).intersection(set(top_10_winter_countries)).intersection(set(top_10_overall_countries))
    common_countries = list(common_countries)
    common_countries.sort()
    return top_10_summer_countries, top_10_winter_countries, top_10_overall_countries, common_countries
    
#q04_find_top_10(OlympicsDFCopy, 'Total_Summer', 'Total_Winter', 'Total')
'''

