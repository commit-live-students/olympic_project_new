# %load q07_unusual_performances/build.py
# default imports
from greyatomlib.olympics_project_new.q02_country_operations.build import q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
data = OlympicsDF[OlympicsDF['Country']!= 'Totals']
low = 0.05
high = 0.95
BetterTeams=['France',
 'Germany',
 'Great Britain',
 'Italy',
 'Soviet Union',
 'Sweden',
 'United States']

WorseTeams=['Bahrain',
 'Barbados',
 'Bermuda',
 'Botswana',
 'Burundi',
 'Ivory Coast',
 'Cyprus',
 'Djibouti',
 'Eritrea',
 'Gabon',
 'Grenada',
 'Guatemala',
 'Guyana',
 'Iraq',
 'Macedonia',
 'Mauritius',
 'Montenegro',
 'Netherlands Antilles',
 'Niger',
 'Paraguay',
 'Senegal',
 'Sudan',
 'Togo',
 'Tonga',
 'United Arab Emirates',
 'Virgin Islands']


def q07_unusual_performances(low,high,data):
    return WorseTeams,BetterTeams






