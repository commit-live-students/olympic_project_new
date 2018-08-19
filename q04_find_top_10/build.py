# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'

OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    

Total_Summer_col = 'Total_Summer'
Total_Winter_col = 'Total_Winter'
Total_col = 'Total'

    
def q04_find_top_10(OlympicsDF=OlympicsDF, Total_Summer_col = Total_Summer_col, Total_Winter_col = Total_Winter_col, Total_col = Total_col):
    ascending_country_names = OlympicsDF.sort_values(by=['Country_Name'], ascending=True)
    
    descending_total_summer = ascending_country_names.sort_values(by=['Total_Summer'], ascending=False)
    descending_total_winter = ascending_country_names.sort_values(by=['Total_Winter'], ascending=False)
    descending_total = ascending_country_names.sort_values(by=['Total'], ascending=False)
    
    top_10_summer = []
    top_10_winter = []
    top_10_total = []
    count = 1
    while (count<=10):
        top_10_summer.append(OlympicsDF.iloc[descending_total_summer.index[count],16])
        top_10_winter.append(OlympicsDF.iloc[descending_total_winter.index[count],16])
        top_10_total.append(OlympicsDF.iloc[descending_total.index[count],16])
        count = count + 1
    common_countries = list(set(top_10_summer).intersection(set(top_10_winter).intersection(top_10_total)))
    return top_10_summer, top_10_winter, top_10_total, common_countries 



