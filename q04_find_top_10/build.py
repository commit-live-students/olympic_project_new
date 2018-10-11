# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(OlympicsDF, p1, p2,p3):
    #OlympicsDF['Country Name'] = OlympicsDF['Country'].str.replace(r'[\(\[].*?[\)\]]','').str.replace(' ','').str.replace(u'\xa0','')
    l1 = list(OlympicsDF.iloc[OlympicsDF.sort_values('Total_Summer', ascending=False).index.tolist()[1:11],-2])
    l2 = list(OlympicsDF.iloc[OlympicsDF.sort_values('Total_Winter', ascending=False).index.tolist()[1:11],-2])
    l3 = list(OlympicsDF.iloc[OlympicsDF.sort_values('Total', ascending=False).index.tolist()[1:11],-2])
    l4 = list(set(l1).intersection(l2,l3))
    return l1,l2,l3,l4


# type(OlympicsDF.sort_values('Total_Summer', ascending=False))#.index(OlympicsDF['Total_Summer']).tolist()
OlympicsDF.index.tolist()
list(OlympicsDF.iloc[OlympicsDF.sort_values('Total', ascending=False).index.tolist()[1:11],-2])
# OlympicsDF.head()


