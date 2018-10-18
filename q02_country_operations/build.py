from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
import pandas as pd
path = './data/olympics.csv'
df = pd.read_csv(path, skiprows=[0])
OlympicsDF=q01_rename_columns(path) 


def q02_country_operations(OlympicsDF):
    OlympicsDF['Country_Name']=(OlympicsDF['Country'].str.split('(').str)[0].str.strip()
    return(OlympicsDF)

q02_country_operations(OlympicsDF)











