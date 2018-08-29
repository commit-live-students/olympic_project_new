# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(olympic , summer_column , winter_column , total_column ):
    top_countries = []
    top_summer_countries = []
    top_winter_countries = []
    common_countries = []
    
    for x in list(olympic[total_column].loc[:144].nlargest(10).index.values):
        top_countries.append(olympic['Country_Name'][x])
    
    for x in list(olympic[summer_column].loc[:144].nlargest(10).index.values):
        top_summer_countries.append(olympic['Country_Name'][x])

    
    for x in list(olympic[winter_column].loc[:144].nlargest(10).index.values):
        top_winter_countries.append(olympic['Country_Name'][x])
    
    common_countries = list(set(top_winter_countries) & set(top_summer_countries) & set(top_countries))
    
    return top_summer_countries, top_winter_countries ,top_countries ,common_countries




