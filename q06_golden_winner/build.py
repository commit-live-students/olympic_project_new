# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter, Top10):
    df_summer = OlympicsDF[OlympicsDF['Country_Name'].isin (Top10Summer)]
    df_summer['Gold_Ratio'] = df_summer['Gold_Summer']/df_summer['Total_Summer']
    variable1= str(list(df_summer.loc[df_summer['Gold_Ratio'] == df_summer['Gold_Ratio'].max()]['Country_Name'])[0])
    
    df_winter = OlympicsDF[OlympicsDF['Country_Name'].isin (Top10Winter)]
    df_winter['Gold_Ratio'] = df_winter['Gold_Winter']/df_winter['Total_Winter']
    variable2= str(list(df_winter.loc[df_winter['Gold_Ratio'] == df_winter['Gold_Ratio'].max()]['Country_Name'])[0])
    
    df_common = OlympicsDF[OlympicsDF['Country_Name'].isin (Top10)]
    df_common['Gold_Ratio'] = df_common['Gold_Total']/df_common['Total']
    variable3= str(list(df_common.loc[df_common['Gold_Ratio'] == df_common['Gold_Ratio'].max()]['Country_Name'])[0])
    
    return variable1,variable2,variable3



