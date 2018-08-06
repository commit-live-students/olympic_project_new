# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df, Total_Summer, Total_Winter, Total):
    df = df.iloc[:len(df)-1,:]
    SummerList = list(df.sort_values('Total_Summer',ascending=False)['Country_Name'][0:10])
    WinterList = list(df.sort_values('Total_Winter',ascending=False)['Country_Name'][0:10])
    Top = list(df.sort_values('Total',ascending=False)['Country_Name'][0:10])
    CommonElements = set(SummerList) & set(WinterList) & set(Top)
    
    return SummerList, WinterList, Top, CommonElements
    
q04_find_top_10(OlympicsDF, OlympicsDF['Total_Summer'], OlympicsDF['Total_Winter'], OlympicsDF['Total'])


