# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')


def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter, Top10):
    Top10Summ=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]

    Top10Wint=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]

    Top10All=OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]

    Top_summ=sorted({row['Country_Name']:int(row['Gold_Summer'])/int(row['Total_Summer']) for index,row in Top10Summ.iterrows()}.items(), key=lambda x: x[1], reverse=True)    
    Top_wint=sorted({row['Country_Name']:int(row['Gold_Winter'])/int(row['Total_Winter']) for index,row in Top10Wint.iterrows()}.items(), key=lambda x: x[1], reverse=True)
    Top_all=sorted({row['Country_Name']:int(row['Gold_Total'])/int(row['Total']) for index,row in Top10All.iterrows()}.items(), key=lambda x: x[1], reverse=True)

    return Top_summ[0][0],Top_wint[0][0],Top_all[0][0]




