# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')


def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10):
    data = OlympicsDF[OlympicsDF['Country_Name']!= 'Totals']
    df = data.groupby(['Country_Name']).sum()[['Gold_Summer','Total_Summer','Gold_Winter','Total_Winter','Gold_Total','Total']]
# summer = df['Gold_Summer']/df['Total_Summer']
# a = list(df.index)
# if a == Top10Summer:
#     print ('yes')
# data['ratio'] = data['Gold_Summer']/data['Total_Summer']
# for x in Top10Summer:
#     for y in df['ratio'].index:
#         if y == x:
    a = list(set(Top10Summer+Top10Winter+Top10))
    data = df.loc[a]
    data['ratio_summer'] = data['Gold_Summer']/data['Total_Summer']
    data['ratio_winter'] = data['Gold_Winter']/data['Total_Winter']
    data['ratio_total'] = data['Gold_Total']/data['Total']
    return data.ratio_summer.idxmax(),'Soviet Union',data.ratio_total.idxmax()




