# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df, column1, column2, column3):
    
    top_summer_rows = df.sort_values('Total_Summer', ascending=False)[1:].head(10)['Country_Name']
    top_winter_rows = df.sort_values('Total_Winter', ascending=False)[1:].head(10)['Country_Name']
    top_total_rows = df.sort_values('Total', ascending=False)[1:].head(10)['Country_Name']
    
    top_summer_rows = list(top_summer_rows)
    top_winter_rows = list(top_winter_rows)
    top_total_rows = list(top_total_rows)
    
    set_top_summer_rows = set(top_summer_rows)
    set_top_winter_rows = set(top_winter_rows)
    set_top_total_rows = set(top_total_rows)
    common_set = set_top_summer_rows.intersection(set_top_winter_rows).intersection(set_top_total_rows)
    return (top_summer_rows, top_winter_rows, top_total_rows, list(common_set))
    

# q04_find_top_10(OlympicsDF, 'Total_Summer', 'Total_Winter', 'Total')    




