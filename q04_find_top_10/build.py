# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df,totalSummer,totalWinter,total):
    df=df.iloc[:len(df)-1,:]
    topSummers = list(df.nlargest(10,totalSummer)['Country_Name'])
    topWinter = list(df.nlargest(10,totalWinter)['Country_Name'])
    topTotal = list(df.nlargest(10,total)['Country_Name'])
    common = list(set(topSummers).intersection(set(topWinter),set(topTotal)))
    return topSummers,topWinter,topTotal,common
    
Top10Summer,Top10Winter, Top10, Common = q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')



