# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(df, Sum, Win, Tot):
    Gold_Ratio= []
    
    
    list_Sum = df.nlargest(10,['Total_Summer'])
    list_Win = df.nlargest(10,['Total_Winter'])
    list_Tot = df.nlargest(10,['Total'])
    Gold_Ratio_1=list(list_Sum.groupby(['Country_Name']).apply(lambda s: s.Gold_Summer/s.Total_Summer).sort_values(ascending = False).head(1).index[0])
    Gold_Ratio_2=list(list_Sum.groupby(['Country_Name']).apply(lambda s: s.Gold_Winter/s.Total_Winter).sort_values(ascending = False).head(1).index[0])
    Gold_Ratio_3=list(list_Sum.groupby(['Country_Name']).apply(lambda s: s.Gold_Total/s.Total).sort_values(ascending = False).head(1).index[0])
    
    return Gold_Ratio_1[0],Gold_Ratio_2[0],Gold_Ratio_3[0]

q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10)




