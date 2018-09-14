# %load q05_top_10_plotting/build.py
# default imports
import matplotlib.pyplot as plt
from greyatomlib.olympics_project_new.q04_find_top_10.build import q04_find_top_10, q03_better_event, q02_country_operations, q01_rename_columns
plt.switch_backend('agg')
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF)    
Top10Summer,Top10Winter, Top10, Common =q04_find_top_10(OlympicsDF,'Total_Summer', 'Total_Winter','Total')
def q05_top_10_plotting(OlympicsDF,Top10,Top10Summer,Top10Winter):
    data = OlympicsDF.iloc[:len(OlympicsDF)-1,:]
    top_ten_winter = data.nlargest(10,'Total_Winter')[['Country_Name','Total_Winter']]
    top_ten_summer = data.nlargest(10,'Total_Summer')[['Country_Name','Total_Summer']]
    top_ten_total = data.nlargest(10,'Total')[['Country_Name','Total']]
    plt.bar(top_ten_total['Country_Name'],top_ten_summer['Total_Summer'])
    plt.bar(top_ten_total['Country_Name'],top_ten_winter['Total_Winter'])
    plt.bar(top_ten_total['Country_Name'],top_ten_total['Total'])
q05_top_10_plotting(OlympicsDF,Top10,Top10Summer,Top10Winter)



