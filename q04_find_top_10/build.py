# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

def q04_find_top_10(df,p1,p2,p3):
    result_summer = df.sort_values(p1, ascending=[0]).iloc[1:,-2].head(10).tolist()
    result_winter = df.sort_values(p2, ascending=[0]).iloc[1:,-2].head(10).tolist()
    result_total = df.sort_values([p3,p1], ascending=[0,0]).iloc[1:,-2].head(10).tolist()
    result_comman = list(set(result_summer).intersection(result_winter, result_total))
    return result_summer,result_winter,result_total,result_comman

q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')


