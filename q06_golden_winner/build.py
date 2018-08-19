# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(df, Top10Summer, Top10Winter, Top10):
    SummerTotal = df[df['Country_Name'].isin(Top10Summer)]
    SummerTotal['Gold_Ratio'] = SummerTotal['Gold_Summer'] / SummerTotal['Total_Summer']
    SummerGoldRatio = list(SummerTotal[SummerTotal['Gold_Ratio'] == SummerTotal['Gold_Ratio'].max()]['Country_Name'])[0]
    
    WinterTotal = df[df['Country_Name'].isin(Top10Winter)]
    WinterTotal['Gold_Ratio'] = SummerTotal['Gold_Winter'] / SummerTotal['Total_Winter']
    WinterGoldRatio = list(WinterTotal[WinterTotal['Gold_Ratio'] == WinterTotal['Gold_Ratio'].max()]['Country_Name'])[0]
    
    Total = df[df['Country_Name'].isin(Top10)]
    Total['Gold_Ratio'] = SummerTotal['Gold_Total'] / SummerTotal['Total']
    TotalGoldRatio = list(Total[Total['Gold_Ratio'] ==Total['Gold_Ratio'].max()]['Country_Name'])[0]

    return SummerGoldRatio, WinterGoldRatio, TotalGoldRatio
    
q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10)


