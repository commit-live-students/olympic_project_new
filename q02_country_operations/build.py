# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)
# def q02_country_operations(df):
def q02_country_operations(df):
    a = df.Country
    b = []
    for x in a:
        b.append(x.split('\xa0'))
    Country_name = []
    for x in b:
        Country_name.append(x[0])

    df['Country_name'] = Country_name
    return df
q02_country_operations(OlympicsDF)


