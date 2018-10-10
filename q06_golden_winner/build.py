# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter,Top10):
    OlympicsDF.drop(OlympicsDF.tail(1).index,inplace=True)
    df1 = OlympicsDF.sort_values('Total_Summer',ascending = False).groupby('Country').head(2).iloc[1:11,:]
    df1['ratio']=df1['Gold_Summer']/df1['Total_Summer']
    str1=df1.nlargest(1,'ratio')['Country_Name'].values.tolist()[0]
    
    df2 = OlympicsDF.sort_values('Total_Winter',ascending = False).groupby('Country').head(2).iloc[1:11,:]
    df2['ratio']=df2['Gold_Winter']/df2['Total_Winter']
    str2=df2.nlargest(1,'ratio')['Country_Name'].values.tolist()[0]
    
    df3 = OlympicsDF.sort_values('Total',ascending = False).groupby('Country').head(2).iloc[1:11,:]
    df3['ratio']=df3['Gold_Total']/df3['Total']
    str3=df3.nlargest(1,'ratio')['Country_Name'].values.tolist()[0]
    
    return str1,str2,str3
    


