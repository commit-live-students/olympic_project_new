# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10):
    df1 = OlympicsDF
    df2 = df1[df1.Country_Name.isin(Top10Summer) ==True]
    df2['gold_ratio_summer'] = df2['Gold_Summer']/df2['Total_Summer']  
    higher_golds_summer = df2.loc[df2['gold_ratio_summer'] == df2['gold_ratio_summer'].max(), 'Country_Name']
    
    df3 = df1[df1.Country_Name.isin(Top10Winter) ==True]
    df3['gold_ratio_winter'] = df3['Gold_Winter']/df3['Total_Winter']  
    higher_golds_winter = df3.loc[df3['gold_ratio_winter'] == df3['gold_ratio_winter'].max(), 'Country_Name']
    
    df4 = df1[df1.Country_Name.isin(Top10Summer) ==True]
    df4['gold_ratio_total'] = df4['Gold_Total']/df4['Total']  
    higher_golds_total = df4.loc[df4['gold_ratio_total'] == df4['gold_ratio_total'].max(), 'Country_Name']
    
    return higher_golds_summer.iloc[0],higher_golds_winter.iloc[0],higher_golds_total.iloc[0]












