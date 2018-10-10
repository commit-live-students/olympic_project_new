# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def q02_country_operations(df=OlympicsDF):
    df['Country_Name']=  df['Country']
    df['Country_Name'] = (df['Country'].str.split('(').str)[0].str.strip()
    df.columns = df.columns.str.replace('\'',' ') 
    return df






q02_country_operations()


