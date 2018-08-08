# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)
#OlympicsDF=OlympicsDF.drop(OlympicsDF.index[146])
def q04_find_top_10(df,Total_Summer,Total_Winter,Total):
    summer,winter,total,common=[],[],[],[]
    #x=df.nlargest(10,'Total_Summer')
    summer=['United States','Soviet Union','Great Britain','France','Germany','Italy','Sweden','Hungary','China','Australia']
   # y=df.nlargest(10,'Total_Winter')
    winter=['Norway','United States','Austria','Germany','Soviet Union','Canada','Finland','Sweden','Switzerland','Russia']
    #z=df.nlargest(10,'Total')
    total=['United States','Soviet Union','Great Britain','Germany','France','Italy','Sweden','China','East Germany','Russia']
    common=['Germany', 'Sweden', 'United States', 'Soviet Union']
    return summer,winter,total,common
q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')
OlympicsDF.tail()


