# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

def q06_golden_winner(variable1, variable2, variable3, variable4):
    
    # result of max ration of gold form Top 10 summer
    var1 = maxRationOfGold(variable1, variable2, '_Summer')
    # result of max ration of gold form Top 10 Winter
    var2 = maxRationOfGold(variable1, variable3, '_Winter')
    # result of max ration of gold form Top 10 Total
    var3 = maxRationOfGold(variable1, variable4, '_Total')
    
    return var1, var2,var3


def maxRationOfGold(df, countries, season):
    result = []
    for element in countries:
        gold = int(df.loc[df['Country_Name']== element]['Gold'+season])
        if '_Total' == season:
            Total = int(df.loc[df['Country_Name']== element]['Total'])
        else:
            Total = int(df.loc[df['Country_Name']== element]['Total'+season])
        r = gold/Total * 100, element
        result.append(r)

    result.sort(reverse=True)
    return result[0][1]


q06_golden_winner(OlympicsDF, Top10Summer, Top10Winter, Top10)



