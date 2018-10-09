# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q06_golden_winner(OlympicsDF , Top10Summer,Top10Winter, Top10):
    variable1 = OlympicsDF [OlympicsDF ['Country_Name'].isin(Top10Summer)]
    variable1['col1'] = (variable1['Gold_Summer']/variable1['Total_Summer'])
    country_summer = variable1.sort_values('col1', axis=0, ascending=False).reset_index(drop =True)['Country_Name'][0]
    
    variable2 = OlympicsDF [OlympicsDF ['Country_Name'].isin(Top10Winter)]
    variable2['col2'] = (variable2['Gold_Winter']/variable2['Total_Winter'])
    country_winter = variable2.sort_values('col2', axis=0, ascending=False).reset_index(drop =True)['Country_Name'][0]
    
    variable3 = OlympicsDF [OlympicsDF ['Country_Name'].isin(Top10)]
    variable3['col3'] = (variable3['Gold_Total']/variable3['Total'])
    country_total = variable3.sort_values('col3', axis=0, ascending=False).reset_index(drop =True)['Country_Name'][0]
    
    return country_summer,country_winter,country_total
    




