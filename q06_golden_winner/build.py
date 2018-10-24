# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter, Top10):
    
#     Top10Summer = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10Summer)].loc[:,['Country_Name', 'Total']]

    Top10Summer = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10Summer)]
    Top10Winter = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10Winter)]
    Top10 = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10)]
    
    Top10Summer['gold_s_ratio'] = Top10Summer['Gold_Summer']
    Top10Summer['gold_s_ratio'] = Top10Summer['Gold_Summer'] / Top10Summer['Total_Summer']
    
    Top10Winter['gold_w_ratio'] = Top10Winter['Gold_Winter']
    Top10Winter['gold_w_ratio'] = Top10Winter['Gold_Winter'] / Top10Winter['Total_Winter']
    
    Top10['gold_b_ratio'] = Top10['Gold_Total']
    Top10['gold_b_ratio'] = Top10['Gold_Total'] / Top10['Total']
    
    gold_s_ratio = Top10Summer.loc[Top10Summer['gold_s_ratio'].idxmax()]['Country_Name']
    gold_w_ratio = Top10Winter.loc[Top10Winter['gold_w_ratio'].idxmax()]['Country_Name']
    gold_b_ratio = Top10.loc[Top10['gold_b_ratio'].idxmax()]['Country_Name']

    return gold_s_ratio, gold_w_ratio, gold_b_ratio
# Top10Winter = OlympicsDF.loc[OlympicsDF.Country_Name.isin(Top10Winter)]
# Top10Winter['gold_w_ratio'] = Top10Winter['Gold_Winter']
# Top10Winter['gold_w_ratio'] = Top10Winter['Gold_Winter'] / Top10Winter['Total_Winter']
# Top10Winter
q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10)    







