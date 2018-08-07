# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
from operator import itemgetter

def q06_golden_winner(q04_find_top_10,Top10Summer,Top10Winter, Top10):
    df=OlympicsDF
    a=df[df['Country_Name'].isin(Top10Summer)]
    b=df[df['Country_Name'].isin(Top10Winter)]
    c=df[df['Country_Name'].isin(Top10)]
    q=[]
    t=[]
    s=[]
    
    for i,j,k in zip(a['Gold_Summer'],a['Total_Summer'],a['Country_Name']):#pass 2 columns as 2 different arguments and not just one argument.
        p=i/j,k
        q.append(p)
    r=sorted(q)
    SummerGoldRatio=max(r)[1]
    
    for i,j,k in zip(b['Gold_Winter'],b['Total_Winter'],b['Country_Name']):
        p=i/j,k
        t.append(p)
    WinterGoldRatio=max(t)[1]
    
    for i,j,k in zip(c['Gold_Total'],c['Total'],c['Country_Name']):
        p=i/j,k
        s.append(p)
    TotalRatio=max(s)[1]

    return str(SummerGoldRatio),str(WinterGoldRatio),str(TotalRatio)
      
        
    
        
        
        
        
        
        
    
    


c=q06_golden_winner(q04_find_top_10,Top10Summer,Top10Winter, Top10)

c


