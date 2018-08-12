# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    

def get_country_name(item):
    return item[0].strip()

def q02_country_operations(df):
    # Extracts country name from 'Country' and creates a new column called 'Country Name'.
    df['Country Name'] = df['Country'].str.split('(')
    df['Country Name'] = df['Country Name'].apply(get_country_name)
    
    return df

# q02_country_operations(OlympicsDF)



