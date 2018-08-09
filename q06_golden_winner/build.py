# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(df, Top10Summer,Top10Winter, Top10):
    
    summer_filtered_df = df.loc[df['Country_Name'].isin(Top10Summer), ['Country_Name', 'Gold_Summer','Total_Summer']]
    summer_filtered_df['Gold_Ratio'] = summer_filtered_df['Gold_Summer'] / summer_filtered_df['Total_Summer']
    max_filtered = summer_filtered_df['Gold_Ratio'].max()
    summer_filtered_df = summer_filtered_df.loc[summer_filtered_df['Gold_Ratio'] == max_filtered]
    city_summer = summer_filtered_df['Country_Name'].values[0]
    
    winter_filtered_df = df.loc[df['Country_Name'].isin(Top10Winter), ['Country_Name', 'Gold_Winter','Total_Winter']]
    winter_filtered_df['Gold_Ratio'] = winter_filtered_df['Gold_Winter'] / winter_filtered_df['Total_Winter']
    max_filtered = winter_filtered_df['Gold_Ratio'].max()
    winter_filtered_df = winter_filtered_df.loc[winter_filtered_df['Gold_Ratio'] == max_filtered]
    city_winter = winter_filtered_df['Country_Name'].values[0]
    
    filtered_df = df.loc[df['Country_Name'].isin(Top10), ['Country_Name', 'Gold_Total','Total']]
    filtered_df['Gold_Ratio'] = filtered_df['Gold_Total'] / filtered_df['Total']
    max_filtered = filtered_df['Gold_Ratio'].max()
    filtered_df = filtered_df.loc[filtered_df['Gold_Ratio'] == max_filtered]
    city_total = filtered_df['Country_Name'].values[0]
    
    return city_summer, city_winter, city_total

# q06_golden_winner(OlympicsDF, Top10Summer,Top10Winter, Top10)





