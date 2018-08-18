# %load q06_golden_winner/build.py
# default imports
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')

#Function definition
def q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter, Top10):
    ''' Function to get the countries who have highest gold ratio as compared to total medals in games'''
    
    #creating new column gold ratio for summer games and getting top country
    OlympicsDF['Gold Ratio'] = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]['Gold_Summer']/OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Summer)]['Total_Summer']
    goldratio_summer = OlympicsDF[['Gold Ratio','Country_Name']].sort_values(by='Gold Ratio',ascending = False).head(1)['Country_Name'].iloc[0]

    #creating new column gold ratio  for winter games and getting top country
    OlympicsDF['Gold Ratio2'] = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]['Gold_Winter']/OlympicsDF[OlympicsDF['Country_Name'].isin(Top10Winter)]['Total_Winter']
    goldratio_winter = OlympicsDF[['Gold Ratio2','Country_Name']].sort_values(by='Gold Ratio2',ascending = False).head(1)['Country_Name'].iloc[0]

    #creating new column gold ratio for both games and getting top country
    OlympicsDF['Gold Ratio3'] = OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]['Gold_Total']/OlympicsDF[OlympicsDF['Country_Name'].isin(Top10)]['Total']
    goldratio_both = OlympicsDF[['Gold Ratio3','Country_Name']].sort_values(by='Gold Ratio3',ascending = False).head(1)['Country_Name'].iloc[0]

    return goldratio_summer,goldratio_winter,goldratio_both

#Function call
q06_golden_winner(OlympicsDF,Top10Summer,Top10Winter, Top10)


