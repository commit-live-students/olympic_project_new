# %load q02_country_operations/build.py
# default imports
from greyatomlib.olympics_project_new.q01_rename_columns.build import q01_rename_columns
#Previous Functions
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    


def SubString(str1):
    str2 = '('
    CharFindPosition = str1.find(str2)
    return_String = str1[:CharFindPosition]
    return return_String.strip()

def q02_country_operations(OlympicsDF):
    #df = (OlympicsDF['Country'].str.extract('([A-Z]\w{0,})', expand=True))
    df = OlympicsDF['Country']
    df = df.apply(SubString)
    OlympicsDF['Country_Name'] = df
    return OlympicsDF



