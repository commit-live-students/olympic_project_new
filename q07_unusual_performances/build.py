# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)

def q07_unusual_performances(OlympicsDF,lq,uq):
    
    #Quant = OlympicsDF.Total.quantile([lq,up])
    #low_quant = Quant.iloc[0]
    #upper_quant = Quant.iloc[1]
    worse_countries = OlympicsDF[OlympicsDF['Total']<=lq].Country_Name
    better_countries = OlympicsDF[OlympicsDF['Total'] > uq].Country_Name
    return worse_countries,better_countries.iloc[:-1]
    
#q07_unusual_performances(OlympicsDF, quant_df.loc[low], quant_df.loc[high])





