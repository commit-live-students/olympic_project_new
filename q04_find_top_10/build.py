# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)
OlympicsDF=OlympicsDF.drop(OlympicsDF.index[146])
def q04_find_top_10(df,Total_Summer,Total_Winter,Total):
    summer,winter,total,common=[],[],[],[]
    x=df.nlargest(10,'Total_Summer')
    summer=x['Country_Name'].tolist()
    y=df.nlargest(10,'Total_Winter')
    winter=y['Country_Name'].tolist() 
    z=df.nlargest(10,'Total')
    total=z['Country_Name'].tolist()
    common=list(set(summer).intersection(set(winter).intersection(set(total))))
    common.sort()
    return summer,winter,total,common
q04_find_top_10(OlympicsDF,"Total_Summer","Total_Winter","Total")


