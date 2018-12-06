# %load q04_find_top_10/build.py
# default imports
from greyatomlib.olympics_project_new.q03_better_event.build import q03_better_event,q02_country_operations, q01_rename_columns
path = './data/olympics.csv'
OlympicsDF=q01_rename_columns(path)    
OlympicsDF=q02_country_operations(OlympicsDF)
OlympicsDF=q03_better_event(OlympicsDF) 

def q04_find_top_10(Dataset, col1, col2, col3):

    #Getting the indices of top 10 countries event wise(viz. Summer, Winter, Total) and storing it in a variable.
    #Dataset.iloc[0:-1,:] --> Excludes the last row which gives the total count. Hence to be excluded in analysis.
    summer_index = Dataset.iloc[0:-1,:].sort_values(by=[col1],ascending=False).head(10).index
    winter_index = Dataset.iloc[0:-1,:].sort_values(by=[col2],ascending=False).head(10).index
    total_index  = Dataset.iloc[0:-1,:].sort_values(by=[col3],ascending=False).head(10).index
    
    #Stores common index in all the above 3 lists
    intersect_index = summer_index.intersection(winter_index).intersection(total_index)

    #Separate list to store countries for each event.
    summer_top_10_Countries = Dataset.loc[summer_index,'Country_Name']
    winter_top_10_Countries = Dataset.loc[winter_index,'Country_Name']
    total_top_10_Countries  = Dataset.loc[total_index,'Country_Name']
    common_Countries        = Dataset.loc[intersect_index,'Country_Name']

    return summer_top_10_Countries,winter_top_10_Countries,total_top_10_Countries,common_Countries

#Call to the function -
q04_find_top_10(OlympicsDF,'Total_Summer','Total_Winter','Total')


