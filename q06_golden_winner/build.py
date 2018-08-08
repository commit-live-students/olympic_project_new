# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def ratio(values):
    pass

def q06_golden_winner(df,p1,p2,p3):
    #Country with best gold ratio in summer
    summer_value = df.loc[df['Country_Name'].isin(p1)]
    summer_ratio = summer_value['Gold_Summer'] / summer_value['Total_Summer']
    topsummercon = summer_value.loc[summer_ratio.argmax()]['Country_Name']
    #Country with best gold ratio in winter
    winter_value = df.loc[df['Country_Name'].isin(p2)]
    winter_ratio = winter_value['Gold_Winter'] / winter_value['Total_Winter']
    topwintercon = winter_value.loc[winter_ratio.argmax()]['Country_Name']
    #Country with best gold ratio in overall
    total_value = df.loc[df['Country_Name'].isin(p3)]
    total_ratio = total_value['Gold_Total'] / total_value['Total']
    toptotalcon = total_value.loc[total_ratio.argmax()]['Country_Name']
    return topsummercon,topwintercon,toptotalcon


