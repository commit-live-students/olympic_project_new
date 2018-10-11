# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF,l1,l2,l3):
    df1 = OlympicsDF[OlympicsDF['Country_Name'].isin(l1)]
    df1['Gold_Ratio'] = df1['Gold_Summer']/df1['Total_Summer']
    var1 = df1[df1.index==df1['Gold_Ratio'].idxmax()].iloc[0,-3]
    df2 = OlympicsDF[OlympicsDF['Country_Name'].isin(l2)]
    df2['Gold_Ratio'] = df2['Gold_Winter']/df2['Total_Winter']
    var2 = df2[df2.index==df2['Gold_Ratio'].idxmax()].iloc[0,-3]
    df3 = OlympicsDF[OlympicsDF['Country_Name'].isin(l3)]
    df3['Gold_Ratio'] = df3['Gold_Total']/df3['Total']
    var3 = df3[df3.index==df3['Gold_Ratio'].idxmax()].iloc[0,-3]
    return var1,var2,var3
df = OlympicsDF
df1 = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]
list(df1)


