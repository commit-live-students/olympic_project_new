# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')


def q06_golden_winner(olympic ,top_summer_countries , top_winter_countries,top_countries ):
    df_top_countries = olympic[olympic['Country_Name'].isin(top_countries)]
    df_top_summer_countries = olympic[olympic['Country_Name'].isin(top_summer_countries)]
    df_top_winter_countries =  olympic[olympic['Country_Name'].isin(top_winter_countries)]

    top_gold_to_total_ratio = df_top_countries['Gold_Total']/df_top_countries['Total']
    summer_gold_to_total_ratio = df_top_countries['Gold_Winter']/df_top_countries['Total_Winter']
    winter_gold_to_total_ratio = df_top_countries['Gold_Summer']/df_top_countries['Total_Summer']

    return olympic['Country_Name'].get_value(top_gold_to_total_ratio.idxmax()) ,olympic['Country_Name'].get_value(summer_gold_to_total_ratio.idxmax()) ,olympic['Country_Name'].get_value(winter_gold_to_total_ratio.idxmax())
    




