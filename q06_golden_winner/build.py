# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(df,Top10Summer,Top10Winter, Top10):
    s=df[df['Country_Name'].isin(Top10Summer)]
    s['Gold_Ratio']=s['Gold_Summer']/s['Total_Summer']
    s_ratio=list(s[s['Gold_Ratio']==s['Gold_Ratio'].max()]['Country_Name'])[0]
    
    w=df[df['Country_Name'].isin(Top10Winter)]
    w['Gold_Ratio']=w['Gold_Winter']/w['Total_Winter']
    w_ratio=list(w[w['Gold_Ratio']==w['Gold_Ratio'].max()]['Country_Name'])[0]
    
    t=df[df['Country_Name'].isin(Top10)]
    t['Gold_Ratio']=s['Gold_Total']/s['Total']
    t_ratio=list(t[t['Gold_Ratio']==t['Gold_Ratio'].max()]['Country_Name'])[0]

    return  s_ratio,w_ratio,t_ratio

q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10)


